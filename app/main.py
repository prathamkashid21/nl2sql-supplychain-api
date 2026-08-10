from fastapi import FastAPI

app = FastAPI(
    title="NL2SQL Supply Chain API",
    description="AI-powered Natural Language to SQL Analytics API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "NL2SQL Supply Chain API",
        "status": "Running Successfully",
        "version": "1.0.0"
    }