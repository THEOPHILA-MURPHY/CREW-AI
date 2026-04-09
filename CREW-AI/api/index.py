from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .crew import create_healthcare_crew
import os

app = FastAPI(title="Healthcare CrewAI API")

class TopicRequest(BaseModel):
    topic: str

@app.post("/api/generate")
async def generate_post(request: TopicRequest):
    if not request.topic:
        raise HTTPException(status_code=400, detail="Topic is required")
        
    try:
        # Initialize and run CrewAI
        crew = create_healthcare_crew(request.topic)
        result = crew.kickoff()
        
        # If result is a CrewOutput object in newer versions, handle it:
        # result typically has a raw string or can be cast to string
        final_text = str(result)
        
        return {"content": final_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Note: Vercel routes `/api/*` to this app object automatically via vercel.json.
