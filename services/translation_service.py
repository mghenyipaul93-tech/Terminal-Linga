
from openai import OpenAI
import os

class TranslationService:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def translate(self, text, target_language):
        if not text:
            raise ValueError("Text to translate cannot be empty.")

        response = self.client.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": f"Translate to {target_language}: {text}"}
        ]
        )    
        
    
        return response.choices[0].message.content.strip()