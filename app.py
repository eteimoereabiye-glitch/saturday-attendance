import streamlit as st
from google import genai
import os

# 1. Setup the AI Client using a secure API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    st.error("Missing Gemini API Key. Please configure it in your Streamlit dashboard settings.")
    st.stop()

client = genai.Client(api_key=api_key)
