# backend.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import io


# Extract text from PDF
def extract_text(file):
    reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# Main matching function
def get_ranked_resumes(job_desc, files):

    resumes = []
    names = []

    for f in files:
        resumes.append(extract_text(f))
        names.append(f.name)

    docs = [job_desc] + resumes

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs)

    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()

    result = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

    return result
