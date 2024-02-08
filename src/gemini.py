import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load All Environment Variables
load_dotenv()

# Configure genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(board, class_, subject, question_type, question):
    prompt_template = """
    You are an expert in solving exam problems and doubts of school students who are preparing for their board and final exams. Your responses are highly accurate and easily understandable for students.
    Your responses always lie within the context of:
    - Board of the student: {board}
    - Class of the student: {class_}
    - Subject of the student: {subject}
    - Question type: {question_type}
    Now, answer the following question: {question}

    Answer:
    """
    
    model = genai.GenerativeModel(model_name="gemini-pro")
    prompt = prompt_template.format(board=board, class_=class_, subject=subject, question_type=question_type, question=question)
    response = model.generate_content(prompt)
    return response.text
