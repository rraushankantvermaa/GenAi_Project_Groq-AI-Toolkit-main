import streamlit as st
import base64
from modules.sentiment_summary import sentiment_app
from modules.keyword_extractor import keyword_app
from modules.structured_json import json_app
from modules.speech_to_text import speech_app
from modules.text_to_speech_groq import text_to_speech_app
from modules.test_to_speech_pyttsx3 import text_to_speech_app

# Page Config
st.set_page_config(
    page_title="Groq AI Suite",
    page_icon="🤖",
    layout="wide"
)

# Video Background & Custom CSS

# Official Streamlit test asset (100% reliable link)
# video_url = "https://static.streamlit.io/examples/star.mp4"

# st.markdown(f"""
# <style>
# /* 1. Force the main Streamlit containers to be transparent so the video is visible */
# .stAppViewContainer, .stMainViewContainer, .stApp {{
#     background-color: transparent !important;
# }}

# /* 2. Style the video element to occupy the full background viewport */
# #bg-video {{
#     position: fixed;
#     right: 0;
#     bottom: 0;
#     min-width: 100%;
#     min-height: 100%;
#     width: auto;
#     height: auto;
#     z-index: -1;
#     object-fit: cover;
#     filter: brightness(0.3); /* Keeps text highly readable */
# }}

# /* 3. Keep the sidebar distinct and readable */
# [data-testid="stSidebar"] {{
#     background-color: rgba(14, 17, 23, 0.9) !important;
#     backdrop-filter: blur(10px);
# }}

# /* Your existing component styles */
# .stButton button {{
#     width:100%;
#     border-radius:10px;
#     height:45px;
# }}

# .card {{
#     padding:20px;
#     border-radius:15px;
#     background-color: rgba(30, 30, 30, 0.75);
#     border:1px solid #333;
#     backdrop-filter: blur(5px);
# }}

# .title {{
#     text-align:center;
#     color:#00D4FF;
# }}
# </style>

# <video autoplay loop muted playsinline id="bg-video">
#   <source src="{video_url}" type="video/mp4">
# </video>
# """, unsafe_allow_html=True)

video_url = "uploads\Background.mp4"

# Local Video Background Processor

def get_video_base64(video_path):
    try:
        with open(video_path, "rb") as video_file:
            encoded_string = base64.b64encode(video_file.read()).decode()
        return f"data:video/mp4;base64,{encoded_string}"
    except FileNotFoundError:
        # Fallback if the local file isn't found in the directory
        return "https://streamlit.io"

# Read your local background file (Make sure 'Background.mp4' is in the same folder as this script)
video_source = get_video_base64("Background.mp4")

# Double braces {{ }} protect CSS syntax from the Python f-string parser
st.markdown(f"""
<style>
/* 1. Force the main Streamlit containers to be transparent so the video is visible */
.stAppViewContainer, .stMainViewContainer, .stApp {{
    background-color: transparent !important;
}}

/* 2. Style the video element to occupy the full background viewport */
#bg-video {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%); /* Centers the video perfectly */
    min-width: 100%;
    min-height: 100%;
    width: 100vw;                      /* Forces it to match viewport width */
    height: 100vh;                     /* Forces it to match viewport height */
    z-index: -1;
    object-fit: cover;                 /* Keeps it full screen without warping */
    object-position: center 20%;       /* Shifts focus up to show the mountains */
    filter: brightness(0.3);           /* Keeps text highly readable */
}}

/* 3. Keep the sidebar distinct and readable */
[data-testid="stSidebar"] {{
    background-color: rgba(14, 17, 23, 0.9) !important;
    backdrop-filter: blur(10px);
}}

/* Your existing component styles */
.stButton button {{
    width:100%;
    border-radius:10px;
    height:45px;
}}

.card {{
    padding:20px;
    border-radius:15px;
    background-color: rgba(30, 30, 30, 0.75);
    border:1px solid #333;
    backdrop-filter: blur(5px);
}}

.title {{
    text-align:center;
    color:#00D4FF;
}}
</style>

<video autoplay loop muted playsinline id="bg-video">
  <source src="{video_source}" type="video/mp4">
</video>
""", unsafe_allow_html=True)




# Sidebar
st.sidebar.title("🚀 Groq AI Suite")

project = st.sidebar.radio(
    "Choose Project",
    [
        "Sentiment Analyzer",
        "Keyword Extractor",
        "Structured JSON",
        "Speech To Text",
        "Text To Speech using Groq",
        "Text To Speech using pyttsx3"
    ]
)

 
# Home Page
if project == "Sentiment Analyzer":
    sentiment_app()

elif project == "Keyword Extractor":
    keyword_app()

elif project == "Structured JSON":
    json_app()

elif project == "Speech To Text":
    speech_app()

elif project == "Text To Speech using Groq":
    text_to_speech_app()

elif project == "Text To Speech using pyttsx3":
    text_to_speech_app()
