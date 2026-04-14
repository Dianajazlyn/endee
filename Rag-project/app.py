import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import io

# ── Page config ──────────────────────────────────────────────
st.set_page_config(page_title="Smart Resume Screener", page_icon="📄")
st.title("📄 Smart Resume Screener")
st.markdown("Upload resumes and enter a job description to find the best match!")

# ── Helper: extract text from PDF ────────────────────────────
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

# ── Upload Resumes ────────────────────────────────────────────
st.header("📂 Step 1: Upload Resumes (PDF)")
uploaded_files = st.file_uploader(
    "Upload one or more resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# ── Job Description ───────────────────────────────────────────
st.header("💼 Step 2: Enter Job Description")
job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="e.g. We are looking for a Python developer with machine learning experience..."
)

# ── Match Button ──────────────────────────────────────────────
if st.button("🔍 Find Best Matches"):
    if not uploaded_files:
        st.warning("Please upload at least one resume!")
    elif not job_description.strip():
        st.warning("Please enter a job description!")
    else:
        st.header("🏆 Results: Best Matching Resumes")

        # Extract text from all resumes
        resumes = []
        names = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resumes.append(text)
            names.append(file.name)

        # TF-IDF Vectorization
        documents = [job_description] + resumes
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Cosine similarity between job description and each resume
        scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        # Sort by score
        ranked = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

        # Display results
        for rank, (name, score) in enumerate(ranked, start=1):
            percent = round(score * 100, 2)
            st.markdown(f"### #{rank} — {name}")
            st.progress(score)
            st.markdown(f"**Match Score: {percent}%**")
            if percent >= 50:
                st.success("✅ Strong Match")
            elif percent >= 25:
                st.warning("⚠️ Moderate Match")
            else:
                st.error("❌ Weak Match")
            st.divider()