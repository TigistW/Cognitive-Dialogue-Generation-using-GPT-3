from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins or use "*" for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input data model
class InputText(BaseModel):
    text: str
@app.get("/")
def welcome():
    return {"Hello"}

@app.post("/chat")
def predict_hate_speech(input_text: InputText):
    preprocessed_text = input_text.text
    return {JSONResponse(content=preprocessed_text)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)