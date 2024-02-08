import streamlit as st
from src.gemini import get_gemini_response
from src.config import configure_streamlit_ui
from src.utils import get_user_input


def main():
    configure_streamlit_ui()

    st.title("PrepGenius - Your Exam Helper")
    st.write("🚀 Unlock Your Potential with PrepGenius: Where Preparation Meets Mastery")
    st.markdown("---")
    
    board, class_, subject, question_type, user_question = get_user_input()
    get_answer = st.button("Get Answer")

    if get_answer and user_question:
        response = get_gemini_response(board, class_, subject, question_type, user_question)
        st.markdown("---")
        st.subheader("Answer:")
        st.write(response)
        st.markdown("---")
        
    
    # Give some top margin
    st.markdown("---")
    # Show credits
    st.subheader("Credits:")
    st.write("Made with ❤️ by [Atul Kumar Gupta](https://www.linkedin.com/in/theatulgupta/)")
    
    # Show my social media account in a row

    st.subheader("Follow us:")
    st.write("[LinkedIn](https://www.linkedin.com/in/theatulgupta/)")
    st.write("[GitHub](https://github.com/theatulgupta)")
    st.write("[YouTube](https://www.youtube.com/@AGKMindsYT)")
    st.write("[Instagram](https://www.instagram.com/_theatulgupta/)") 
    st.write("© 2024 PrepGenius. All rights reserved.")
    st.markdown("---")
 

if __name__ == "__main__":
    main()
