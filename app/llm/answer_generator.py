from app.llm.gemini import generate_text


def generate_answer(question: str, sql: str, results):

    prompt = f"""
You are a supply-chain analytics assistant.

Answer the user's question using ONLY the database results provided below.

USER QUESTION:
{question}

SQL QUERY:
{sql}

DATABASE RESULTS:
{results}

RULES:

1. Answer the user's question directly.
2. Do not invent information.
3. Do not introduce facts that are not present in the results.
4. If the results are empty, say that no matching data was found.
5. Keep the answer concise and understandable.
6. Use appropriate formatting for numbers.
7. Do not mention that you are an AI.
"""

    return generate_text(prompt).strip()