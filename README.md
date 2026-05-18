# 🤖 DocuMind AI Assistant

An AI-powered PDF Question Answering Chatbot built using Retrieval-Augmented Generation (RAG), LangChain, FAISS, HuggingFace Embeddings, Groq LLM, and Streamlit.

Users can upload PDF documents and ask questions directly from the document using an interactive ChatGPT-like interface.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 AI-powered question answering
- 🔍 Semantic search using FAISS vector database
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 ChatGPT-like chat interface
- 📂 Recent file history
- 🔎 Search uploaded files
- 📥 Download AI responses
- 📋 Copy responses easily
- 🎨 Professional Streamlit UI
- ⚡ Fast Groq LLM integration

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq API
- PyPDFLoader
- RAG Architecture

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/PoreddiArpitha/PDF-RAG-CHATBOT.git
cd PDF-RAG-CHATBOT
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add API Key

Create a `.env` file in the project folder and add:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:

https://console.groq.com/

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open browser:

```bash
http://localhost:8501
```

---

## 🧠 RAG Workflow

```text
Upload PDF
     ↓
Extract Text
     ↓
Split into Chunks
     ↓
Generate Embeddings
     ↓
Store in FAISS Vector Database
     ↓
User Question
     ↓
Retrieve Relevant Chunks
     ↓
Generate AI Response
```

---

## 📂 Project Structure

```bash
PDF-RAG-CHATBOT/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files/folders
├── .env                   # API keys and environment variables
```

---


## 📸 Screenshots
<h3>Preview</h3>
<img
src="https://i.postimg.cc/TwWpwmDM/IMG-20260518-WA0001.jpg" width="800">

---

## 🌟 Future Improvements

* 🎤 Voice Assistant
* 🌐 Online Deployment
* 🧾 Multiple PDF Support
* 🔐 Authentication System
* 💾 Chat Memory
* 📱 Mobile Responsive UI

---

## 👩‍💻 Author

### Poreddi Arpitha

GitHub:
https://github.com/PoreddiArpitha/PDF-RAG-CHATBOT.git

---

## 📄 License

This project is licensed under the MIT License.

























