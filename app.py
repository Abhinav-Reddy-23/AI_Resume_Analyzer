import streamlit as st
import PyPDF2
import matplotlib.pyplot as plt

# Page Settings
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

# Title
st.title("📄 AI Resume Analyzer")

# File Upload
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf")

# Main Logic
if uploaded_file is not None:

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    # Show Resume Content
    st.subheader("Resume Content")
    st.write(text)

    # Skills List
    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "aws",
        "react",
        "javascript",
        "c++",
        "data science",
        "html",
        "css",
        "tensorflow",
        "pandas",
        "numpy"
    ]

    # Detect Skills
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Show Skills
    st.subheader("Detected Skills")

    for skill in found_skills:
        st.success(skill)

    # ATS Score
    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.subheader("ATS Score")

    st.progress(score)

    st.write(score, "/ 100")

    # Resume Rating
    st.subheader("Suggestions")

    if score >= 80:
        st.success("Excellent Resume")

    elif score >= 50:
        st.info("Good Resume")

    else:
        st.warning("Needs Improvement")

    # Skill Chart
    st.subheader("Skills Chart")

    skill_count = len(found_skills)
    missing_skills = len(skills) - skill_count

    labels = ["Detected Skills", "Missing Skills"]
    values = [skill_count, missing_skills]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct='%1.1f%%')

    st.pyplot(fig)
        # Recommended Skills
    st.subheader("Recommended Skills")

    recommended_skills = []

    if "python" not in found_skills:
        recommended_skills.append("python")

    if "sql" not in found_skills:
        recommended_skills.append("sql")

    if "machine learning" not in found_skills:
        recommended_skills.append("machine learning")

    if "data science" not in found_skills:
        recommended_skills.append("data science")

    if "react" not in found_skills:
        recommended_skills.append("react")

    if recommended_skills:

        for skill in recommended_skills:
            st.info(skill)

    else:
        st.success("Your resume contains most important skills")
            # Job Role Prediction
    st.subheader("Predicted Job Role")

    if "machine learning" in found_skills and "python" in found_skills:
        st.success("AI Engineer")

    elif "react" in found_skills and "javascript" in found_skills:
        st.success("Frontend Developer")

    elif "sql" in found_skills and "data science" in found_skills:
        st.success("Data Analyst")

    elif "java" in found_skills:
        st.success("Java Developer")

    else:
        st.info("Software Developer")