from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, yuta!"}

@app.get("/123")
def create():
    return{"ok": True}