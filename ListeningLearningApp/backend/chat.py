from huggingface_hub import InferenceClient
import streamlit as st
from typing import Optional, Dict, Any


# Initialize Hugging Face InferenceClient
client = InferenceClient(
    provider="nebius",
    api_key={"Authorization"}
)


class HuggingFaceChat:
    def __init__(self, model: str = "deepseek-ai/DeepSeek-R1"):
        """Initialize Hugging Face Chat Client"""
        self.model = model

    def generate_response(self, message: str, max_tokens: int = 500) -> Optional[str]:
        """Generate a response using Hugging Face's API"""
        messages = [{"role": "user", "content": message}]

        try:
            completion = client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
            )
            return completion.choices[0].message["content"]

        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            return None


if __name__ == "__main__":
    chat = HuggingFaceChat()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            break
        response = chat.generate_response(user_input)
        print("Bot:", response)
