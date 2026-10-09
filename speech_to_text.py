import streamlit as st
import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_audio_info(filename, data):
    """
    Detect the actual audio format from the file bytes.
    This prevents problems when a file has the wrong extension.
    """

    # MP3
    if data.startswith(b"ID3"):
        return "mp3", "audio/mpeg"

    # WAV
    if data.startswith(b"RIFF") and data[8:12] == b"WAVE":
        return "wav", "audio/wav"

    # OGG
    if data.startswith(b"OggS"):
        return "ogg", "audio/ogg"

    # FLAC
    if data.startswith(b"fLaC"):
        return "flac", "audio/flac"

    # WebM / Matroska
    if data.startswith(b"\x1a\x45\xdf\xa3"):
        return "webm", "audio/webm"

    # MP4 / M4A
    if len(data) > 12 and data[4:8] == b"ftyp":
        return "m4a", "audio/mp4"

    # Fall back to extension
    ext = os.path.splitext(filename)[1].lower()

    mime_types = {
        ".mp3": ("mp3", "audio/mpeg"),
        ".wav": ("wav", "audio/wav"),
        ".m4a": ("m4a", "audio/mp4"),
        ".ogg": ("ogg", "audio/ogg"),
        ".webm": ("webm", "audio/webm"),
        ".flac": ("flac", "audio/flac"),
        ".mp4": ("mp4", "audio/mp4"),
    }

    return mime_types.get(ext, ("unknown", "application/octet-stream"))


def speech_app():

    st.header("🎤 Speech To Text")

    audio = st.file_uploader(
        "Upload an audio file",
        type=[
            "mp3",
            "wav",
            "m4a",
            "ogg",
            "webm",
            "flac",
            "mp4"
        ]
    )

    if audio:

        # Read uploaded file ONCE
        audio_bytes = audio.getvalue()

        st.audio(audio_bytes)

        st.write("### File information")

        st.write("**Filename:**", audio.name)
        st.write("**Streamlit MIME type:**", audio.type)
        st.write("**File size:**", len(audio_bytes), "bytes")

        # Detect actual format
        detected_format, detected_mime = get_audio_info(
            audio.name,
            audio_bytes
        )

        st.write("**Detected format:**", detected_format)
        st.write("**Detected MIME:**", detected_mime)

        if st.button("🎙️ Transcribe"):

            try:

                st.info("Sending audio to Groq...")

                # IMPORTANT:
                # Explicitly tell Groq:
                # filename + bytes + MIME type

                filename = f"recording.{detected_format}"

                file_payload = (
                    filename,
                    audio_bytes,
                    detected_mime
                )

                transcription = client.audio.transcriptions.create(
                    file=file_payload,
                    model="whisper-large-v3-turbo",
                    response_format="json",
                    language="en",
                    temperature=0.0
                )

                st.success("Transcription completed!")

                st.subheader("📝 Transcription")

                st.write(transcription.text)

            except Exception as e:

                st.error("Transcription failed!")

                st.exception(e)