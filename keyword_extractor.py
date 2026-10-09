import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def keyword_app():

    st.title("🔑 Keyword Extractor")

    text = st.text_area("Enter Text")

    if st.button("Extract Keywords"):

        prompt = f"""
        Extract 10 important keywords:

        {text}
        """

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        result = response.choices[0].message.content

        st.write(result)