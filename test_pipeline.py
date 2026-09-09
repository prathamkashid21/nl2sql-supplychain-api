from app.database.db import SessionLocal
from app.services.nl2sql import process_question


question = "What are the top 5 products by sales?"

db = SessionLocal()

try:

    result = process_question(
        question,
        db
    )

    print("\nQUESTION:")
    print(result["question"])

    print("\nGENERATED SQL:")
    print(result["sql"])

    print("\nRESULTS:")

    for row in result["results"]:
        print(row)

    print("\nANSWER:")
    print(result["answer"])

finally:

    db.close()