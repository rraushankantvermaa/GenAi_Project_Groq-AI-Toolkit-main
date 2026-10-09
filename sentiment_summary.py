import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)


# Streamlit UI

def sentiment_app():

    st.title("😊 Sentiment Analyzer")

    st.write("Enter some text and let AI analyze it.")


    # Text input
    text = st.text_area(
        "Enter your text:",
        height=200,
        placeholder="Example: I really enjoyed this movie. The story was amazing!"
    )


    # Analyze button
    if st.button("Analyze Text"):

        if text.strip() == "":
            st.warning("Please enter some text.")

        else:

            prompt = f"""
                    Analyze the following text.

                    Text:
                    {text}

                    Give the answer in this exact format:

                    Sentiment: Positive/Negative/Neutral
                    Topic: <main topic>
                    Summary: <short summary>
                    """

            # Call Groq
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # Get response text
            result = response.choices[0].message.content

            # Display result
            st.subheader("Analysis")
            st.write(result)