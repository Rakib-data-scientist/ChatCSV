import streamlit as st
from utils import get_answer_csv

def display_header():
    """Display the header of the Streamlit application."""
    st.header("Interact with your pandas dataframe")

def upload_file():
    """Allow user to upload a CSV file and return the uploaded file."""
    return st.file_uploader("Upload a pandas dataframe", type=["csv"])

def get_user_query():
    """Prompt the user to enter a query and return the input."""
    return st.text_area("Ask any question related to the dataframe")

def main():
    """Main function to orchestrate the Streamlit application flow."""
    display_header()
    uploaded_file = upload_file()
    
    if uploaded_file:
        query = get_user_query()
        if st.button("Submit"):
            st.write(get_answer_csv(uploaded_file, query))

if __name__ == "__main__":
    main()
