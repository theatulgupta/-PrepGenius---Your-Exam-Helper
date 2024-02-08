import streamlit as st

def get_user_input():
    board_options = ["CBSE", "ICSE", "Madhya Pradesh State Board"]
    class_options = [str(i) for i in range(1, 13)]  # Generate class options dynamically
    subject_options = ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", "Economics", "Geography", "History", "Hindi", "English", "Political Science", "Psychology", "Sociology"]
    question_type_options = ["Numerical", "Theoretical", "MCQ", "Fill in the Blank", "Short Answer", "Long Answer"]

    col1, col2 = st.columns(2)
    
    with col1:
        board = st.selectbox("Board", board_options)
        subject = st.selectbox("Subject", subject_options)
    
    with col2:
        class_ = st.selectbox("Class", class_options,index=11)
        question_type = st.selectbox("Question Type", question_type_options)
    
    user_question = st.text_input("Ask your question:")
    
    return board, class_, subject, question_type, user_question
