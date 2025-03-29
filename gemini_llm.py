from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-1.5-pro',temperature=0.9)

# result = model.invoke()


st.header("chat with AI")

user = st.text_input("Enter your message", key="input")

if st.button("Submit"):
    with st.spinner("Generating response..."):
        result = model.invoke(user)
        st.write("AI response:")
        st.write(result.content)
