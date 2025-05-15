from fastapi import FastAPI
from app.pipeline import process_text
from app.models import TextRequest, LocationResponse

app = FastAPI()

@app.post("/extract_locations", response_model=LocationResponse)
def extract_locations(request: TextRequest):
    result = process_text(request.text)
    return LocationResponse(entities=result)