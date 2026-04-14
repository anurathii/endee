<p align="center">
  <h1>📘 AI Study Assistant</h1>
</p>

<p align="center">
  <b>An AI-powered Study Assistant using Retrieval-Augmented Generation (RAG) for answering questions from study materials.</b>
</p>

<p align="center">
  <a href="https://github.com/yourusername/ai-study-assistant">
    <img src="https://img.shields.io/badge/Project-AI_Study_Assistant-blue?style=flat-square" />
  </a>
  <a href="https://github.com/endee-io/endee">
    <img src="https://img.shields.io/badge/Vector_DB-Endee-success?style=flat-square" />
  </a>
</p>

---

# 🧠 Overview

**AI Study Assistant** is a lightweight Retrieval-Augmented Generation (RAG) system that helps students get instant answers from stored study notes.

It uses a vector database (**:contentReference[oaicite:0]{index=0}**) to store embeddings of study materials and retrieves relevant context before generating answers using an AI model.

---

# 🚀 Key Features

- 📚 Stores study notes as embeddings  
- 🔍 Semantic search using vector database  
- 🤖 AI-generated answers using retrieved context  
- ⚡ Fast and lightweight implementation  
- 🧠 RAG-based architecture  

---

# ⚙️ System Workflow

1. Study notes are collected  
2. Notes are converted into embeddings  
3. Embeddings are stored in **:contentReference[oaicite:1]{index=1}**  
4. User asks a question  
5. Most relevant notes are retrieved  
6. AI generates answer using retrieved context  

---

# 🛠️ Tech Stack

- Python  
- OpenAI API (or any LLM)  
- Endee Vector Database  
- RAG (Retrieval-Augmented Generation)

---

# 📁 Project Structure

ai-study-assistant/
│
├── app.py
├── requirements.txt
└── README.md

---

# ▶️ How to Run

# 1. Install dependencies

```bash
pip install -r requirements.txt

---

# 2.Run the project

python app.py

---


# Example Usage

Input:
What is Machine Learning?
Output:
Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data...

---

#📌 Requirements

endee
openai

---

#🧠 Use of Endee

This project uses Endee as the vector database to:

Store embeddings of study notes
Perform similarity search
Retrieve relevant context for AI responses

---

#📊 Why This Project?

Demonstrates RAG architecture
Shows real-world AI application
Uses vector database concepts
Simple but powerful for learning

---

#⚠️ Future Improvements

Add PDF upload support
Add Streamlit UI
Expand dataset size
Multi-user chat interface

---

#📄 License

This project is for educational purposes.

---

# 👨‍💻Author

Your Anurathi L
GitHub: https://github.com/anurathii
