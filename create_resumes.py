from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(filename, content):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    y = height - 40

    for line in content.split("\n"):
        c.drawString(40, y, line)
        y -= 15

    c.save()

# Folder path
output_folder = "sample_data/resumes"
os.makedirs(output_folder, exist_ok=True)

# Resume 1 - Fresher
resume1 = """Name: Isha Manoria
Education: B.Tech Computer Science 2027
Skills: Python, SQL, Java, Basic ML, Excel
Projects: Chatbot, Result Analysis System
Objective: Entry-level software/data role"""

create_pdf(os.path.join(output_folder, "fresher_resume.pdf"), resume1)

# Resume 2 - Data Analyst
resume2 = """Name: Mokshit Khemsara
Skills: SQL, Python, Pandas, Power BI, C++
Experience: Data Analyst Intern at ABC Corp
Projects: Sales Dashboard, Churn Analysis"""

create_pdf(os.path.join(output_folder, "data_analyst_resume.pdf"), resume2)

# Resume 3 - ML Engineer
resume3 = """Name: Parth Pathak
Skills: Python, TensorFlow, Scikit-learn, NLP, AI
Experience: ML Intern at AI Labs
Projects: Spam Classifier, Image Recognition"""

create_pdf(os.path.join(output_folder, "ml_engineer_resume.pdf"), resume3)

print("PDF Resumes Created Successfully!")