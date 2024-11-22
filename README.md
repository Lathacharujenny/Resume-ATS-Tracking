# ATS Tracking System
!['ATS Tracting System']('Image/image.png')

An intelligent **Applicant Tracking System (ATS)** that uses Google Generative AI and Streamlit to provide insights and recommendations on resume-job description alignment.

## Features

- **Resume Analysis**: Upload a PDF resume, and the system evaluates it against a provided job description.
- **Key Features**:
  - **Tell Me About Resume**: Get professional evaluation and insights.
  - **Percentage Match**: Calculate the matching percentage between the resume and job description.
  - **Keypoints in Resume**: Extract key technical and soft skills, educational details, and experience.
  - **Match with Job Description**: Generate a comparison table highlighting strengths and weaknesses.
  - **Keywords Missing**: Identify and suggest keywords from the job description absent in the resume.
- **AI-Powered**: Powered by Google Generative AI (Gemini model) for advanced content generation.

## Technologies Used

- **Streamlit**: For building an interactive user interface.
- **Google Generative AI**: To process and evaluate the content.
- **PyPDF2**: For reading and extracting text from PDF resumes.
- **dotenv**: For securely managing API keys and environment variables.

## Installation and Setup

### Prerequisites

- Python 3.8 or above
- A Google API Key for Generative AI
- Render account for deployment

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ats-tracking.git
   cd ats-tracking
