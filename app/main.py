from fastapi import FastAPI

from app.api.query import router as query_router


app = FastAPI(
    title="Intelligent Natural Language to SQL API",
    description="AI-powered supply chain analytics using natural language queries.",
    version="1.0.0"
)


app.include_router(query_router)


@app.get("/")
def root():
    return {
        "message": "NL2SQL Supply Chain API is running"
    }