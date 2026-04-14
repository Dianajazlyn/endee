# app.py

import streamlit as st
from backend import get_ranked_resumes

st.set_page_config(page_title="Smart Resume Screener", page_icon="📄")

st.title("📄 Smart Resume Screener")
st.write("Upload resumes and compare with job description")

# Upload resumes
files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# Job description
job_desc = st.text_area("Enter Job Description")

# Button
if st.button("Find Matches 🔍"):

    if not files:
        st.warning("Please upload resumes")
    elif not job_desc.strip():
        st.warning("Please enter job description")
    else:

        results = get_ranked_resumes(job_desc, files)

        st.header("🏆 Results")

        for i, (name, score) in enumerate(results, 1):
            percent = round(score * 100, 2)

            st.markdown(f"### {i}. {name}")
            st.progress(float(score))
            st.write(f"Match: {percent}%")

            if percent > 50:
                st.success("Strong Match")
            elif percent > 25:
                st.warning("Moderate Match")
            else:
                st.error("Weak Match")

            st.divider()
