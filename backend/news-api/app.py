from fastapi import FastAPI

app = FastAPI()

@app.get("/news/headlines")
def read_news():
    return {"headlines": ["News API running successfully!"]}

