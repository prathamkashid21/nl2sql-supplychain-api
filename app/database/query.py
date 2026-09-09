from sqlalchemy import text
from sqlalchemy.orm import Session

from app.validators.sql_validator import validate_sql


def execute_query(db: Session, sql: str):

    validate_sql(sql)

    try:
        result = db.execute(text(sql))

        columns = list(result.keys())

        rows = [
            dict(zip(columns, row))
            for row in result.fetchall()
        ]

        return rows

    except Exception as e:
        raise ValueError(
            f"SQL execution failed: {str(e)}"
        )