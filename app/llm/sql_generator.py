from app.llm.gemini import generate_text
from app.database.schema import get_schema_text


def generate_sql(question: str) -> str:

    schema = get_schema_text()

    prompt = f"""
You are an expert SQLite SQL generator for a supply-chain analytics system.

Your job is to convert a natural-language question into ONE valid SQLite SELECT query.

DATABASE SCHEMA:

{schema}

IMPORTANT RULES:

1. Use ONLY tables and columns present in the schema.
2. Use SQLite-compatible SQL.
3. Only generate SELECT queries.
4. Do NOT generate INSERT.
5. Do NOT generate UPDATE.
6. Do NOT generate DELETE.
7. Do NOT generate DROP.
8. Do NOT generate ALTER.
9. Do NOT generate CREATE.
10. Do NOT generate ATTACH.
11. Do NOT generate DETACH.
12. Do NOT generate PRAGMA.
13. Do NOT generate multiple SQL statements.
14. Do not invent tables or columns.
15. Use JOINs when information exists across multiple tables.
16. Return ONLY SQL.
17. Do not use markdown code fences.
18. For questions asking about late orders or late delivery, prefer
    orders.late_delivery_risk = 1 when counting late orders.
19. For sales, use order_items.sales.
20. For profit, use order_items.profit_per_order.
21. Product names are in products.product_name.
22. Customer segments are in customers.customer_segment.
23. Shipping time is orders.days_for_shipping_real.

If the question cannot be answered using this database, return exactly:

UNSUPPORTED_QUERY

USER QUESTION:

{question}
"""

    sql = generate_text(prompt).strip()

    # Remove accidental markdown formatting
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql