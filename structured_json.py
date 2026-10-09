import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def json_app():

    st.title("📦 Structured Output")

    text = st.text_area("Enter Text")

    if st.button("Generate JSON"):

        prompt = f"""
        Return JSON only.

        {{
            "sentiment":"",
            "topic":"",
            "summary":"",
            "keywords":""
        }}

        Text:
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

        st.json(result)