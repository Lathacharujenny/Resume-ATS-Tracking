import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text


def get_text_from_input_pdf(pdf_file):
    reader = pdf.PdfReader(pdf_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text+=str(page.extract_text())

    return text


# Streamlit App
st.set_page_config(page_title='ATS Tracking Expert')
st.header('ATS Tracking System')
input_text_job_description = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF).....", type=['pdf'])

if uploaded_file is not None:
    st.write('File uploaded Successfully')

submit1 = st.button('Tell Me About Resume')
submit2 = st.button('Percentage Match')
submit3 = st.button('Keypoints in Resume')
submit4 = st.button('Match with Job Description')
submit5 = st.button('Keywords Missing in my Resume based on Job Description')

input_prompt1 = """ You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements."""

input_prompt2 = """You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts."""

input_prompt3 = """Extract technical skills, soft skills, education details, and experience/project information directly from the resume. Only include information explicitly stated in the resume for each category.
"""

input_prompt4 = """Given a resume and a job description, generate a table illustrating the match. Use cues to represent high, medium, and low match areas, highlighting strengths and weaknesses"""

input_prompt5 = """Analyze a resume and job description. Identify keywords and skills from the job description absent in the resume. Prioritize based on frequency and relevance to the job. Provide suggestions for integrating these keywords into the resume, emphasizing achievements and quantifiable results"""

def process_request(uploaded_file, input_prompt, job_description):
    pdf_content = get_text_from_input_pdf(uploaded_file)
    response = get_gemini_response(input_text_job_description, pdf_content, input_prompt)
    st.header('The Response is')
    return response



if submit1:
    response = process_request(uploaded_file, input_prompt1, input_text_job_description)
    st.write(response)
elif submit2:
    response = process_request(uploaded_file, input_prompt2, input_text_job_description)
    st.write(response)
elif submit3:
    response = process_request(uploaded_file, input_prompt3, input_text_job_description)
    st.write(response)
elif submit4:
    response = process_request(uploaded_file, input_prompt4, input_text_job_description)
    st.write(response)
elif submit5:
    response = process_request(uploaded_file, input_prompt5, input_text_job_description)
    st.write(response)

