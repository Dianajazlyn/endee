# 📄 Smart Resume Screener

A semantic resume screening tool built using AI and Endee Vector Database.

## 🎯 Project Overview
This project helps HR teams automatically match resumes to job descriptions using semantic similarity. Upload multiple PDF resumes, enter a job description, and the system ranks resumes by relevance.

## 🧠 How It Works
1. Upload PDF resumes
2. Extract text using PyPDF2
3. Convert text to vectors using TF-IDF
4. Match against job description using cosine similarity
5. Display ranked results with match scores

## 🗄️ Use of Endee Vector Database
Endee is used as the vector database backend to store and retrieve resume vectors efficiently for semantic search.

## 🛠️ Tech Stack
- Python
- Streamlit (UI)
- scikit-learn (TF-IDF Vectorization)
- PyPDF2 (PDF text extraction)
- Endee (Vector Database)

## ⚙️ Setup Instructions
1. Clone this repository
2. Install dependencies:
   pip install streamlit scikit-learn PyPDF2
3. Run the app:
   streamlit run app.py

## 💡 Use Case
Smart HR tool for screening and ranking candidates automatically.
    















