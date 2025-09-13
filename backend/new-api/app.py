from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to News API 🚀. Try /news/headlines"}

@app.get("/news/headlines")
def get_headlines():
    return {
        "headlines": [
            "Breaking: K8s-Powered App Launches 🚀",
            "Docker makes local dev simple 🐳",
            "Microservices are the future 🔥"
        ]
    }
