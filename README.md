````markdown
# 🚀 Groq AI Toolkit

> A modular AI-powered Streamlit application that brings together **NLP, Generative AI, Speech AI, and Structured AI outputs** in one interactive dashboard.

<p align="center">
  <img src="outputs/Sentiment_Analyzer.png" width="800">
</p>

<p align="center">
  <strong> Built with Python • Streamlit • Groq API • GPT OSS • Whisper • pyttsx3 • python-dotenv </strong>
</p>

---

## 🌟 About The Project

**Groq AI Toolkit** is a multi-feature AI application built with Python and Streamlit.

Instead of creating separate applications for every AI task, this project brings multiple AI utilities together inside one dashboard.

The application currently includes:

- 📝 Sentiment Analysis
- 🔑 Keyword Extraction
- 📊 Structured JSON Output
- 🎤 Speech To Text
- 🔊 Text To Speech

The project was built as a hands-on exploration of **Generative AI APIs, NLP, speech processing, structured outputs, Python modules, Streamlit UI development, and API integration**.

---

# ✨ Features

| Feature               | Technology               | What It Does                                   |
| --------------------- | ------------------------ | ---------------------------------------------- |
| 📝 Sentiment Analyzer | Groq + LLM               | Analyzes the sentiment of text                 |
| 🔑 Keyword Extractor  | Groq + LLM               | Extracts important keywords from text          |
| 📊 Structured JSON    | Groq + Structured Output | Converts natural language into structured JSON |
| 🎤 Speech To Text     | Groq + Whisper           | Converts uploaded audio into text              |
| 🔊 Text To Speech     | pyttsx3                  | Converts text into spoken audio locally        |

---

# 🏗️ Architecture

The application follows a **modular architecture**.

The main Streamlit application acts as the entry point and routes the user's selection to the appropriate module.

```text
                         ┌─────────────────────┐
                         │      USER           │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Streamlit UI     │
                         │       app.py        │
                         └──────────┬──────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
              ┌─────────┐      ┌─────────┐      ┌─────────┐
              │  Text   │      │  Audio  │      │  Text   │
              │  Tasks  │      │  Tasks  │      │  Speech │
              └────┬────┘      └────┬────┘      └────┬────┘
                   │                │                │
          ┌────────┼────────┐       │                │
          ▼        ▼        ▼       ▼                ▼
     Sentiment  Keywords  JSON   Whisper          pyttsx3
          │        │        │       │                │
          └────────┴────────┘       │                │
                   │                │                │
                   ▼                ▼                ▼
                Groq API       Speech → Text     Text → Audio
```
````

---

# 🔄 Application Flow

## Text-Based AI Features

```text
User enters text
       │
       ▼
Streamlit
       │
       ▼
Groq API
       │
       ▼
Language Model
       │
       ▼
AI Result
       │
       ▼
Streamlit Output
```

The same basic API architecture is reused for different NLP tasks.

---

## 🎤 Speech To Text

```text
Audio File
    │
    ▼
Streamlit Upload
    │
    ▼
Groq API
    │
    ▼
Whisper
    │
    ▼
Transcribed Text
```

---

## 🔊 Text To Speech

The current working implementation uses **pyttsx3** locally.

```text
User Text
    │
    ▼
pyttsx3
    │
    ▼
System Voice
    │
    ▼
WAV Audio
    │
    ▼
Streamlit Audio Player
```

This implementation does not require a separate cloud TTS API.

---

# 📝 1. Sentiment Analyzer

The Sentiment Analyzer accepts text from the user and uses a Groq-hosted language model to analyze its sentiment.

### Example Input

```text
I absolutely loved this laptop! The performance is extremely fast,
the battery lasts all day, and the display is beautiful.
```

### Example Output

```text
Sentiment: Positive
```

The module can also be extended to provide additional information such as:

- Sentiment
- Topic
- Summary
- Keywords
- Explanation

### 📸 Output

![Sentiment Analyzer](outputs/Sentiment_Analyzer.png)

### 💻 Code

[👉 View the source code](modules/sentiment_summary.py)

---

# 🔑 2. Keyword Extractor

The Keyword Extractor identifies important words and phrases from user-provided text.

### Example Input

```text
Artificial intelligence is transforming healthcare,
finance, education and customer service.
```

### Example Output

```text
Artificial Intelligence
Healthcare
Finance
Education
Customer Service
```

### 📸 Output

![Keyword Extractor](outputs/Keyword_Extractor.png)

### 💻 Code

[👉 View the source code](modules/keyword_extractor.py)

---

# 📊 3. Structured JSON

The Structured JSON module demonstrates how an LLM can transform natural language into predictable structured data.

### Example Input

```text
John is 25 years old and works as a software engineer.
He lives in Kolkata.
```

### Example Output

```json
{
  "name": "John",
  "age": 25,
  "profession": "Software Engineer",
  "location": "Kolkata"
}
```

Structured output is useful when AI-generated information needs to be consumed by another program.

For example:

```text
Natural Language
       ↓
       LLM
       ↓
Structured JSON
       ↓
Python / Database / API
```

### 📸 Output

![Structured Output](outputs/Structured_Output.png)

### 💻 Code

[👉 View the source code](modules/structured_json.py)

---

# 🎤 4. Speech To Text

The Speech To Text module allows the user to upload an audio recording.

The uploaded audio is processed using **Groq's Whisper speech-recognition model**.

### Example

```text
🎤 Audio

"Hello, my name is John.
Today I am testing the speech to text application."
```

becomes:

```text
Hello, my name is John.
Today I am testing the speech to text application.
```

### Workflow

```text
🎤 Recording
     │
     ▼
Audio Upload
     │
     ▼
Groq Whisper
     │
     ▼
📝 Transcription
```

### 📸 Output

![Speech To Text](outputs/Speech_To_Text.png)

### 💻 Code

[👉 View the source code](modules/speech_to_text.py)

---

# 🔊 5. Text To Speech

The Text To Speech feature converts text into spoken audio.

The current working implementation uses **pyttsx3**, allowing the application to generate speech locally using the voices available on the system.

### Example

```text
Artificial intelligence is changing the way
we interact with computers.
```

⬇️

```text
🔊 Generated Speech
```

### Workflow

```text
Text
 │
 ▼
pyttsx3
 │
 ▼
System Voice
 │
 ▼
.wav File
 │
 ▼
Streamlit Audio Player
```

### 📸 Output

![Text To Speech](outputs/Text_To_Speech_pyttsx3.png)

### 💻 Code

[👉 View the source code](modules/test_to_speech_pyttsx3.py)

---

# 🖼️ Application Screenshots

## 📝 Sentiment Analyzer

![Sentiment Analyzer](outputs/Sentiment_Analyzer.png)

---

## 🔑 Keyword Extractor

![Keyword Extractor](outputs/Keyword_Extractor.png)

---

## 📊 Structured JSON

![Structured Output](outputs/Structured_Output.png)

---

## 🎤 Speech To Text

![Speech To Text](outputs/Speech_To_Text.png)

---

## 🔊 Text To Speech

![Text To Speech](outputs/Text_To_Speech_pyttsx3.png)

---

# 🧩 Project Structure

```text
Groq-AI-Toolkit/
│
├── app.py
├── getmodels.py
├── test.py
├── requirements.txt
├── .gitignore
├── .env
│
├── modules/
│   ├── keyword_extractor.py
│   ├── sentiment_summary.py
│   ├── speech_to_text.py
│   ├── structured_json.py
│   ├── test_to_speech_pyttsx3.py
│   ├── text_to_speech_groq.py
│   └── ...
│
├── outputs/
│   ├── generated_speech_pyttsx3.wav
│   ├── Keyword_Extractor.png
│   ├── Sentiment_Analyzer.png
│   ├── Speech_To_Text.png
│   ├── Structured_Output.png
│   └── Text_To_Speech_pyttsx3.png
│
└── uploads/
    ├── Background.mp4
    └── Recording.mp3
```

---

# 🛠️ Tech Stack

### Programming

- 🐍 Python

### Frontend

- 🎨 Streamlit

### AI

- 🤖 Groq API
- 🧠 LLMs
- 🎤 Whisper

### Text To Speech

- 🔊 pyttsx3

### Configuration

- 🔐 python-dotenv

### Development Tools

- Git
- GitHub
- VS Code

---

# 🔐 Environment Variables

The Groq API key is stored in a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/cloudsony999/Groq-AI-Toolkit
```

## 2. Open the Project

```bash
cd Groq-AI-Toolkit
```

## 3. Create a Virtual Environment

```bash
python -m venv sentiment-detection-summarizer-ai
```

## 4. Activate the Virtual Environment

### Windows

```bash
sentiment-detection-summarizer-ai\Scripts\activate
```

### Linux / macOS

```bash
source sentiment-detection-summarizer-ai/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure the API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📦 Dependencies

The main dependencies are maintained in:

[👉 `requirements.txt`](requirements.txt)

The project uses packages such as:

```text
streamlit
groq
python-dotenv
pyttsx3
pydub
```

---

# 🧠 What This Project Demonstrates

This project was built as a practical way to learn how different AI capabilities can be integrated into a Python application.

### 🐍 Python

- Functions
- Modules
- File handling
- Exception handling
- Environment variables
- External libraries

### 🎨 Streamlit

- Web UI development using Python
- Sidebar navigation
- Text input
- Buttons
- File upload
- Audio playback
- Interactive application design

### 🤖 Generative AI

- LLM API integration
- Prompt engineering
- Model selection
- Structured output
- NLP tasks
- AI-powered text processing

### 🎤 Speech AI

- Audio file handling
- Speech recognition
- Whisper
- Text-to-Speech
- Local audio generation

### 🔌 API Development

- API authentication
- API requests
- API responses
- Error handling
- Model availability
- Environment configuration

### 🌱 Git & GitHub

- Repository management
- `.gitignore`
- Secret management
- Version control
- Project documentation

---

# 🎯 Future Scope

The following are **future ideas**, not features currently implemented in this project.

They are listed here as possible directions for future development.

## 🤖 AI Chatbot

Add a conversational AI interface with:

- Chat history
- Context-aware conversations
- Streaming responses
- System prompts
- Multiple conversations

---

## 📄 PDF Analyzer

Allow users to upload documents and ask questions about their contents.

```text
PDF
 │
 ▼
Text Extraction
 │
 ▼
Chunking
 │
 ▼
LLM
 │
 ▼
Answer
```

---

## 🎨 Text To Image

Add an image-generation model that can convert prompts such as:

```text
A futuristic city at night with neon lights
```

into generated images.

---

## 🎬 Text To Video

Add an AI video-generation pipeline where users provide a text prompt and receive a generated video.

---

## 🎙️ Voice AI Assistant

Combine the existing speech components with an LLM:

```text
🎤 User Voice
      │
      ▼
  Whisper
      │
      ▼
     LLM
      │
      ▼
  AI Response
      │
      ▼
   TTS Engine
      │
      ▼
🔊 Assistant Voice
```

---

## ☁️ Cloud Deployment

Deploy the application so that it can be accessed through the internet.

Possible deployment targets include:

- Streamlit Community Cloud
- Render
- Railway
- Hugging Face Spaces
- Other cloud platforms

---

# 🗺️ Current Project → Future Roadmap

```text
                 GROQ AI TOOLKIT
                        │
                        ▼
              ┌───────────────────┐
              │ Current Features  │
              └─────────┬─────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
   📝 NLP Tasks     🎤 Speech        🔊 TTS
        │               │                │
        ├─ Sentiment    └─ Whisper      └─ pyttsx3
        ├─ Keywords
        └─ JSON

                        │
                        ▼
              ┌───────────────────┐
              │   Future Ideas    │
              └─────────┬─────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
   🤖 Chatbot      📄 PDF AI       🎨 Image AI
        │
        ▼
   🎬 Video AI
        │
        ▼
   🎙️ Voice Assistant
        │
        ▼
   ☁️ Cloud Deployment
```

> **The roadmap above represents planned/future possibilities only. These features are not currently implemented.**

---

# 🤝 Contributing

Contributions are welcome!

If you have an idea for improving the project:

### 1. Fork the repository

```bash
git fork https://github.com/cloudsony999/Groq-AI-Toolkit
```

### 2. Create a feature branch

```bash
git checkout -b feature/my-new-feature
```

### 3. Make your changes

### 4. Commit your changes

```bash
git add .
git commit -m "Add new AI feature"
```

### 5. Push your branch

```bash
git push origin feature/my-new-feature
```

### 6. Open a Pull Request

Feel free to improve the UI, add AI capabilities, optimize the code, improve documentation, or suggest new features.

---

# ⭐ Like The Project?

If you find **Groq AI Toolkit** useful or interesting:

⭐ **Star the repository**

🍴 **Fork the repository**

🐛 **Report bugs**

💡 **Suggest features**

🤝 **Contribute**

📢 **Share it with others**

Every star and contribution helps! ❤️

---

# 👩‍💻 Author

## Amitava Chatterjee (Trainer in AI Domain)

**GitHub:** [@latenightcoder-git](https://github.com/cloudsony999)

> Built with curiosity, experimentation, and a lot of Python. 🐍🤖

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to:

- Use the project
- Study the code
- Modify the code
- Build upon it
- Share your modifications

Please retain the original attribution.

---

# ❤️ Final Note

This project started as an exploration of individual AI capabilities and gradually evolved into a single modular AI toolkit.

The goal is simple:

> **Learn AI by actually building with it.**

More features can be added as the project grows.

If you like the project, don't forget to ⭐ **Star** and 🍴 **Fork** the repository!

---

<p align="center">

### 🚀 Built with Python + Streamlit + Groq

**Learn • Build • Experiment • Improve**

</p>
```
