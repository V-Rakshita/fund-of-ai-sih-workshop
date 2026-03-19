

# 📌 Intelligent Enterprise Assistant

### AI-driven Chatbot for Organizational Efficiency (SIH1706)

---

## 🚀 Overview

The **Intelligent Enterprise Assistant** is an AI-powered chatbot designed to streamline internal communication and improve efficiency within large organizations.

It leverages **Natural Language Processing (NLP)** and **Deep Learning** to answer employee queries related to:

* HR policies
* IT support
* Company events
* General organizational information

The system also includes **document processing capabilities**, allowing users to upload files and extract insights such as summaries and keywords.

---

## 🎯 Problem Statement

Develop a scalable chatbot that:

* Understands and responds to employee queries
* Processes and analyzes documents
* Supports multiple users simultaneously
* Ensures security via 2-Factor Authentication
* Filters inappropriate language

---

## 🧠 Key Features

### 💬 Smart Chatbot

* Natural language understanding
* Instant responses to employee queries
* Domain-specific knowledge (HR, IT, events)

---

### 📄 Document Processing

* Upload PDF documents
* Automatic text extraction
* Document summarization
* Keyword extraction

---

### 🔐 2-Factor Authentication (2FA)

* Email-based OTP verification
* Secure login system

---

### ⚡ Fast & Scalable

* Handles multiple users (minimum 5 concurrent users)
* Response time < 5 seconds

---

### 🚫 Content Moderation

* Filters abusive or inappropriate language
* Ensures professional interaction

---

## 🏗️ System Architecture

```
Frontend (React / UI)
        │
        ▼
Backend API (FastAPI)
        │
 ┌───────────────┬───────────────┐
 │               │               │
Chatbot Engine   Document AI   Authentication
 │               │               │
NLP Model     PDF Processing     OTP System
 │               │               │
Knowledge Base  Summarizer     Email Service
```

---

## 🛠️ Tech Stack

### 👨‍💻 Backend

* Python
* FastAPI

### 🤖 AI / NLP

* Basic NLP / LLM-ready structure
* (Optional: LangChain, OpenAI, FAISS)

### 📄 Document Processing

* PyPDF2
* NLTK / Regex

### 🔐 Authentication

* OTP-based Email Verification

### 💾 Database (Optional Upgrade)

* PostgreSQL / MongoDB
* Vector DB (FAISS / Pinecone)

---

## 📂 Project Structure

```
enterprise-chatbot/
│
├── main.py                  # FastAPI server
├── auth.py                  # OTP authentication
├── chatbot.py               # Chatbot logic
├── document_processor.py    # PDF processing
├── badwords.py              # Language filter
├── requirements.txt
│
├── data/
│   └── hr_policy.txt        # Knowledge base
│
└── uploads/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/enterprise-chatbot.git
cd enterprise-chatbot
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the server

```bash
uvicorn main:app --reload
```

---

### 4️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

### 🔐 Authentication

**Login (Generate OTP)**

```
POST /login
```

**Verify OTP**

```
POST /verify
```

---

### 💬 Chatbot

```
POST /chat
```

---

### 📄 Upload Document

```
POST /upload
```

---

## 🎬 Demo Flow

1. User logs in using email
2. Receives OTP and verifies identity
3. Starts chatting with the bot
4. Uploads a document
5. Receives:

   * Summary
   * Keywords

---

## 📊 Sample Queries

* “What is the leave policy?”
* “How to reset VPN password?”
* “What are company events?”
* “Summarize this document”

---

## 🔮 Future Enhancements

* Advanced AI (RAG-based chatbot)
* Voice assistant integration
* Slack / Microsoft Teams integration
* Role-based access control
* Analytics dashboard

---

## 👥 Team

* Team Name: *[Your Team Name]*
* Hackathon: Smart India Hackathon (SIH)

---

## 🏆 Conclusion

This project demonstrates how AI can transform internal enterprise systems by:

* Reducing manual workload
* Improving employee experience
* Providing instant, accurate information

---

## 📜 License

This project is for educational and hackathon purposes.


Just tell me 👍
