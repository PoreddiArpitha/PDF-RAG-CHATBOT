import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import tempfile

# Load environment variables
load_dotenv()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.sidebar.title("🤖 DocuMind")

st.sidebar.button("➕ New Chat")

st.sidebar.markdown("---")

st.sidebar.subheader("📂 Search Files")

search_query = st.sidebar.text_input(
    "Search uploaded PDFs"
)
st.sidebar.markdown("---")

st.sidebar.info(
    "RAG Chatbot using LangChain, FAISS, HuggingFace & Groq LLM"
)

st.sidebar.markdown("---")

st.sidebar.subheader("🕘 Recent Chats")

# Initialize recent chats
if "recent_chats" not in st.session_state:
    st.session_state.recent_chats = []

# Filter chats based on search
filtered_chats = []

for chat in st.session_state.recent_chats:

    if search_query.lower() in chat.lower():
        filtered_chats.append(chat)

# Display filtered chats
for chat in filtered_chats:
    st.sidebar.write(f"📄 {chat}")
  
# Streamlit title
st.title("🤖 DocuMind AI Assistant")
st.caption("Smart PDF Question Answering using RAG")

# Upload PDF
uploaded_file = st.file_uploader(
    "📎 Upload your PDF document",
    type=["pdf"]
)

if uploaded_file:

    st.write("Uploaded File:", uploaded_file.name)
    # Save uploaded filename to recent chats
    if uploaded_file.name not in st.session_state.recent_chats:
     st.session_state.recent_chats.insert(
        0,
        uploaded_file.name
     )

    # Save PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings()

    # Store vectors
    vectorstore = FAISS.from_documents(docs, embeddings)

    st.toast("PDF uploaded successfully!")

    # Ask question
    question = st.chat_input(
        "Ask anything from the uploaded PDF..."
    )

    if question:

        # Search similar chunks
        matching_docs = vectorstore.similarity_search(question)

        # Groq model
        llm = ChatGroq(
            model_name="llama-3.1-8b-instant"
        )

        # Combine retrieved text
        context = "\n".join(
            [doc.page_content for doc in matching_docs]
        )

        # Prompt
        prompt = f"""
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {question}
        """

        try:
            response = llm.invoke(prompt)

            st.chat_message("user").write(question)

            st.chat_message("assistant").write(
                response.content
            )

            # Save chat history
            st.session_state.messages.append(
                {"role": "user", "content": question}
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response.content
                }
            )

            # Copy button
            st.code(response.content)

            # Download button
            st.download_button(
                label="⬇ Download Answer",
                data=response.content,
                file_name="answer.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")