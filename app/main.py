from fastapi import FastAPI
from app.routes import sample_routes

app = FastAPI()

# Include routes
app.include_router(sample_routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI app!"}