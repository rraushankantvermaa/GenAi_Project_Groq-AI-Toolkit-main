import streamlit as st
from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def text_to_speech_app():

    st.header("🔊 Text To Speech")

     
    # Frontend: User enters text
     

    text = st.text_area(
        "Enter text you want to convert into speech:",
        placeholder="Type something here...",
        height=150
    )

     
    # Voice selection
     

    voice = st.selectbox(
        "Choose a voice:",
        [
            "autumn",
            "diana",
            "hannah",
            "austin",
            "daniel",
            "troy"
        ]
    )

     
    # Generate speech
     

    if st.button("🎙️ Generate Speech"):

        if not text.strip():

            st.warning("Please enter some text.")

        elif len(text) > 200:

            st.error(
                f"Your text has {len(text)} characters. "
                "Orpheus currently accepts a maximum of 200 characters per request."
            )

        else:

            try:

                with st.spinner("Generating speech..."):

                    response = client.audio.speech.create(
                        model="canopylabs/orpheus-v1-english",
                        voice=voice,
                        response_format="wav",
                        input=text
                    )

                    # Get audio bytes
                    audio_data = response.read()

                st.success("Speech generated successfully!")

                # Play audio in Streamlit
                st.audio(
                    audio_data,
                    format="audio/wav"
                )

                # Download button
                st.download_button(
                    label="⬇️ Download Audio",
                    data=audio_data,
                    file_name="generated_speech_groq.wav",
                    mime="audio/wav"
                )

            except Exception as e:

                st.error("Something went wrong!")
                st.exception(e)