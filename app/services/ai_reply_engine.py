import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_reply(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message['content']
