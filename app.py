import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your Gemini API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # ← Make sure to update your .env file
genai.configure(api_key=api_key)

# Configure Streamlit page
st.set_page_config(page_title="Code Explainer", layout="centered")

# App header
st.title("💬 Code Explainer using Gemini ")
st.markdown("Paste Python or JavaScript code and get a beginner-friendly explanation.")

# Language selector and code input
language = st.selectbox("Select Language", ["Python", "JavaScript"])
code = st.text_area("Enter your code snippet", height=200, placeholder="e.g., def add(a, b): return a + b")

# When user clicks the button
if st.button("Explain Code"):
    if not code.strip():
        st.warning("⚠️ Please enter some code.")
    else:
        with st.spinner("Analyzing code..."):
            try:
                model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
                prompt = f"Explain this {language} code in a simple and beginner-friendly way:\n\n{code}"
                response = model.generate_content(prompt)
                st.success("🧠 Explanation:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
