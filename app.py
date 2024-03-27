from fastapi import FastAPI

VERSION = "0.0.4"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "version": VERSION}