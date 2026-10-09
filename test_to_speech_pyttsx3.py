import streamlit as st
import pyttsx3
import tempfile
import os


def text_to_speech_app():

    st.header("🔊 Text To Speech")

    text = st.text_area(
        "Enter text to convert into speech",
        placeholder="Type something here..."
    )

    if st.button("🎙️ Generate Speech"):

        if not text.strip():
            st.warning("Please enter some text.")
            return

        try:
            # Create TTS engine
            engine = pyttsx3.init()

            # Optional: control speaking speed
            engine.setProperty("rate", 150)

            # Create temporary WAV file
            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".wav"
            )

            audio_path = temp_file.name
            temp_file.close()

            # Generate speech
            engine.save_to_file(text, audio_path)
            engine.runAndWait()

            # Show generated audio
            with open(audio_path, "rb") as audio_file:
                audio_data = audio_file.read()

            st.success("Speech generated successfully!")

            st.audio(
                audio_data,
                format="audio/wav"
            )

            # Download button
            st.download_button(
                label="⬇️ Download Audio",
                data=audio_data,
                file_name="generated_speech_pyttsx3.wav",
                mime="audio/wav"
            )

            # Delete temporary file
            os.remove(audio_path)

        except Exception as e:
            st.error(f"Error generating speech: {e}")