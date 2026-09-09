from app.llm.sql_generator import generate_sql


questions = [
    "What are the top 5 products by sales?",
    "What are the top 5 products by profit?",
    "What are the sales by customer segment?",
    "What is the average shipping time by shipping mode?",
    "How many orders were late?"
]


for question in questions:

    print("\n" + "=" * 70)

    print("QUESTION:")
    print(question)

    print("\nGENERATED SQL:")

    try:
        sql = generate_sql(question)
        print(sql)

    except Exception as e:
        print("ERROR:", e)