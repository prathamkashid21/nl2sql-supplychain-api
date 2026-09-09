from sqlalchemy.orm import Session

from app.llm.sql_generator import generate_sql
from app.database.query import execute_query
from app.llm.answer_generator import generate_answer


def process_question(
    question: str,
    db: Session
):

    # Step 1: Natural language → SQL
    sql = generate_sql(question)

    # Step 2: SQL validation + execution
    results = execute_query(db, sql)

    # Step 3: Results → natural language
    answer = generate_answer(
        question,
        sql,
        results
    )

    return {
        "question": question,
        "sql": sql,
        "results": results,
        "answer": answer
    }