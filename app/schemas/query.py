from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Natural language question about the supply chain database"
    )


class QueryResponse(BaseModel):
    question: str
    sql: str
    results: list