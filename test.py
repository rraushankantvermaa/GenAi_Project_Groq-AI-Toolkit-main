from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()

for model in models.data:
    if "orpheus" in model.id.lower():
        print(model.id)


print("Calling Orpheus...")

response = client.audio.speech.create(
    model="canopylabs/orpheus-v1-english", # in preview 
    voice="autumn",
    input="Hello, this is a test.",
    response_format="wav"
)

response.write_to_file("test.wav")

print("SUCCESS!")
print("Created test.wav")