from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.query import QueryRequest, QueryResponse
from app.services.nl2sql import process_question


router = APIRouter(
    prefix="/api/v1",
    tags=["NL2SQL"]
)


@router.post(
    "/query",
    response_model=QueryResponse
)
def natural_language_query(
    request: QueryRequest,
    db: Session = Depends(get_db)
):

    try:

        result = process_question(
            request.question,
            db
        )

        return result

    except RuntimeError as e:

        if "quota" in str(e).lower():
            raise HTTPException(
                status_code=429,
                detail=str(e)
            )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        print(f"Unexpected error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        )