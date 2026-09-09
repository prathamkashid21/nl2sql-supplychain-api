import re


FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "ATTACH",
    "DETACH",
    "REPLACE",
    "TRUNCATE",
    "PRAGMA",
]


def validate_sql(sql: str):

    if not sql:
        raise ValueError("Generated SQL is empty.")

    sql_clean = sql.strip()

    if sql_clean.upper() == "UNSUPPORTED_QUERY":
        raise ValueError(
            "This question cannot be answered using the supply chain database."
        )

    # Only SELECT statements
    if not re.match(r"^\s*SELECT\b", sql_clean, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed.")

    # Prevent multiple statements
    statements = [
        statement.strip()
        for statement in sql_clean.split(";")
        if statement.strip()
    ]

    if len(statements) > 1:
        raise ValueError("Multiple SQL statements are not allowed.")

    # Block dangerous SQL keywords
    for keyword in FORBIDDEN_KEYWORDS:

        pattern = rf"\b{keyword}\b"

        if re.search(pattern, sql_clean, re.IGNORECASE):
            raise ValueError(
                f"Forbidden SQL operation detected: {keyword}"
            )

    return True