import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDTg9-3QBora9rl0XVRQADtEbtuW5IYo9o")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Chat APP")

question = st.text_input("Ask something")

if st.button("Ask AI"):
    response = model.generate_content(question)
    st.write(response.text)