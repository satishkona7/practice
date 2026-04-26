from fastapi import FastAPI
from app.routes import sample_routes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME"))

# Include routes
app.include_router(sample_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI app!"}