from fastapi import FastAPI
from src.routes import base, placeholder

app = FastAPI()

app.include_router(base.router)
app.include_router(placeholder.router)


@app.get("/")
async def root():
    return {"message": "Hello world!"}
