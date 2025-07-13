import google.generativeai as genai
import os 
from dotenv import load_dotenv 
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model= genai.GenerativeModel('gemini-1.5-flash')
def get_ai_score(about_text):
    try:
        prompt=f"Rate this company’s AI readiness from 1 to 10 based on this description:{about_text}"
        response = model.generate_content(prompt)
        messages=[{"role": "user", "content":prompt}] 
        return response.text
    except Exception as e:
          
        return f"Error: {str(e)}"