import os
import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("AI Chatbot")

# User input section
user_input = st.text_input("Enter your message:", value="Hello, how are you?")

# Generate button
if st.button("Send"):
    try:
        # Call the generative AI model to generate a response
        response = genai.generate_text(
            model="gemini-1.5-flash-8b",
            prompt=user_input,
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192
        )
        st.subheader("Response")
        st.write(response['text'])

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")