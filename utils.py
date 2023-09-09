from typing import TextIO
import os
import openai
import pandas as pd
import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI

# Setting up openai API key from streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def read_csv_file(file: TextIO) -> pd.DataFrame:
    """
    Reads data from a CSV file into a pandas DataFrame.

    Args:
        file (TextIO): The CSV file to read data from.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file)

def create_agent(df: pd.DataFrame) -> "Agent":
    """
    Creates a Langchain agent with the specified dataframe.

    Args:
        df (pd.DataFrame): The dataframe to base the agent on.

    Returns:
        Agent: A Langchain agent.
    """
    return create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Retrieves an answer to a query based on data in a CSV file.

    Args:
        file (TextIO): The CSV file containing the data.
        query (str): The query to find an answer to.

    Returns:
        str: The answer to the query based on the data in the CSV file.
    """
    df = read_csv_file(file)
    agent = create_agent(df)
    return agent.run(query)

# Streamlit UI
if __name__ == "__main__":
    st.title("CSV Query Agent")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        query = st.text_input("Enter your query:")
        if query:
            st.write(get_answer_csv(uploaded_file, query))
