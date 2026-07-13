from fastapi import FastAPI

app = FastAPI(
    title="Non-Profit Decision Intelligence MVP",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Non-Profit Decision Intelligence MVP"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }