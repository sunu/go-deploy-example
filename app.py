from fastapi import FastAPI

VERSION = "0.0.8"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "version": VERSION}