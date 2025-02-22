import streamlit as st
from huggingface_hub import InferenceClient
from typing import Optional
import sys
import os
import json
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.chat import HuggingFaceChat
# Streamlit app
st.title("Chat with AI")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    chat = HuggingFaceChat()
    response = chat.generate_response(user_input)
    st.text_area("AI: ", response)