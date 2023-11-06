from pathlib import Path 

import streamlit as st 
from PIL import Image

# --- PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"  / "main.css"
resume_file = current_dir / "assets" / "JCS-Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


PAGE_TITLE = "Digital CV | Jermaine Samuels"
PAGE_ICON = "🔖"
NAME = "Jermaine Samuels"
DESCRIPTION = """Experienced Data Engineer and Data Scientist with a strong background in Business Analytics with a 
focus on building interactive and data intensive applications."""
EMAIL = "jc.samuels21@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jc-samuels-data-scientist01/",
    "GitHub": "https://github.com/jjsammii"
}

PROJECTS = {
    "🏆 Farmgate Dashboard - Datavisualtion tool for crop prices and price prediction": "https://lnkd.in/ej6Cuwmz",
    "🏆 Tech Talk demo - Youtube Azure Datafactory ETL and Azure machine learning" : "https://www.youtube.com/watch?v=mWW-OsELCn0&t=1892s",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ---LOAD CSS, PDF & PROFIL PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)


#---- Column Section ----
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# ---- Links for social media -----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("-----")

# ---- Projects
st.write("#")
st.subheader("Projects & Accomplishments")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# ---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifictions")
st.write("#")
st.write("💡", "**Data Engineer | Fujitsu Caribbean Limited** Nov 2020 – Present")
st.write(
"""
-   ✔ Scripted unique on-premise data transformation solutions for clients using Python.
-   ✔ Conducted requirements gathering sessions and proposed relevant data architectures.
-   ✔ Built reliable and scalable ETL pipelines using Azure Data Factory, Databricks, Synapse Analytics and Azure Data Lake Gen2 Storage.
-   ✔ Utilized Git and Azure DevOps Git to manage code base and pipeline deployment across multiple environments.
-   ✔ Delivered high quality, production ready pipelines for an array of projects for enterprise clients such as RedStripe Jamaica Limited and National Water Commission Jamaica.
-   ✔ Evaluated client documentation and technical requirements to implement data lakehouse solutions.
-   ✔ Implemented departmental and global data analytics dashboards for clients using PowerBI. 
-   ✔ Built Proof of concept designs for azure cloud architecture and included data governance framework using open-source tools such as datahub.
"""
)

st.write("#")
st.write("💡", "**Business Analyst • Guardsman Limited** Jul 2017 – Nov 2020")
st.write(
"""
-	✔ Generated departmental KPI reports for accounts receivables, billing and collections department.
-   ✔ Lead and conducted in depth analysis of business performance versus business goals.
-   ✔ Established relationships across disparate data sources and datasets for executive dashboards and data warehouse needs.
-   ✔ Automated report generation with macro scripts within excel and python for csv generation.
-   ✔ Created solution to track and tag unapplied cash to stimulate invoice generation using CRON tasks and pdf scraping. 
-   ✔ Collected and documented requirements for departmental business and data analytics.
-   ✔ Redefined standard operating procedures for generating bad debt reports for the receivables and finance department.
-   ✔ Significantly reduced operational delay and vehicle dispatch reporting with task automation scripts with python.
"""
)

st.write("#")
st.write("💡","**Data Scientist • University of the West Indies (Co-Op)** May 2021 – Aug 2021")
st.write(
"""
-   ✔ Built a Jupyter notebook deployment via viola to predict and segment gliomas using convoluted neural network and hosted the models on premise using a .h5 file.
-   ✔ Performed natural language processing of scholarly articles to define how cnn may be improved by contrasting additional features from MRI scans. 

"""
)

# ---- Skill sets
st.write("#")
st.subheader("Skills")
st.write(
"""
-   💻  Programming: Python (Scikit-Learn, Pandas), SQL, R, Scala.
-   📊 Data Visualization: PowerBI, MS EXcel, Plotly, Tableau
-   📈 Modeling: Logistic Regression, Random Forest, tensorflow CNN, etc.
-   💿 Databases: Postgres, MySQL, MongoDB, SQL, NoSQL
-   📚 Platforms and Fremeworks: Azure, Databricks, DataHub, BigQuery, AWS, GitHub

"""
)

# ---- Education
st.write("#")
st.subheader("Education")
st.write("📜", "Niagara College TSoM (May 2023 - Dec 2023) | **Certificate in Internation Business Management**")
st.write("📜", "University of the West Indies (Sep 2019 - Sep 2021) | **Masters in Applied Data Science**")
st.write("📜", "University of the West Indies (Sep 2017 - Sep 2018) | **Post Graduate Diploma in IT**")
st.write("📜", "University of the West Indies (Sep 2009 - Sep 2013) | **Bsc in Chemistry and Marine Biology**")

# ---- CERTIFICATIONS
st.write("#")
st.subheader("Certifications")
st.write("📑", "Amazon Web Services | **Cloud Practitioner**")
st.write("📑", "Microsoft Certified | **Azure Data Engineer Associate**")
st.write("📑", "Microsoft Certified | **Power BI Data Analyst Associate**")
st.write("📑", "Microsoft Certified | **Azure AI Fundamentals**")
st.write("📑", "Microsoft Certified | **Azure Data Fundamentals**")



