from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

st.title("Vocabulary Extractor using Gemini")
paragraph = st.text_area("Enter a paragraph:")

if st.button("Extract Vocabulary"):
    prompt = f"Extract the vocabulary words from the following paragraph:\n\n{paragraph}\n\nReturn only the words as a list."
    
    # Call the Gemini model
    response = llm.invoke(prompt)

    st.write("Vocabulary:")
    st.json(response.content if hasattr(response, 'content') else response)
