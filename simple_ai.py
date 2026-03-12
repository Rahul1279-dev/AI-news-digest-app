import os

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=api_key
                        )

response = model.invoke("How are you?")
response_str =  response.content[0]['text']
print(response_str)