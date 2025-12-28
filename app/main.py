import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from google.generativeai import genai
from app.schemas import QuestionRequest, AnswerResponse
from app.prompts import SYSTEM_PROMPT

load_dotenv

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

app  = FastAPI(
    title = "Gemini Business Q&A API",
    description = "AI-powered question answering for businesses and students",
    version = "1.0.0"
)

@app.post("/ask", response_model=AnswerResponse)
def ask_question(data: QuestionRequest):
    try:
        full_prompt = f"""
        {SYSTEM_PROMPT}
        context: 
            {data.context or "General"}
        User Question:
            {data.question}
        """
        response = model.generate_content(full_prompt)
        return {"answer": response.text}
    except Exception as e:
        raise HTTPException(status_code=500,details=str(e))
    
    