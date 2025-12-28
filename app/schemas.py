from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str
    context: str | None = None
    
class AnswerResponse(BaseModel):
    answer : str