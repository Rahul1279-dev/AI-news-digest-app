import os
import requests
from dotenv import load_dotenv
from send_email import send_email
from langchain.chat_models import init_chat_model

load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")
api_key = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key=api_key
                        )
# topic = "tesla"
url = (f"https://newsapi.org/v2/top-headlines?"
       f"country=us&"
       f"category=business&"
       f"apiKey={news_api_key}&"
       f"language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
articles = content['articles']

# AI summarizing the news
prompt = f"""
Highlight the key points and make it readable:
{articles}
"""

response = model.invoke(prompt)

body =  response.content[0]['text']
body = "Subject: AI News Digest" + "\n" + body
body = body.encode("utf-8")
send_email(message=body)