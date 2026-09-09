from sqlalchemy import inspect
from app.database.db import engine


def get_database_schema():
    inspector = inspect(engine)

    schema = {}

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)

        schema[table_name] = [
            {
                "name": column["name"],
                "type": str(column["type"])
            }
            for column in columns
        ]

    return schema


def get_schema_text():
    schema = get_database_schema()

    lines = []

    for table_name, columns in schema.items():
        lines.append(f"TABLE: {table_name}")

        for column in columns:
            lines.append(
                f"  - {column['name']} ({column['type']})"
            )

        lines.append("")

    return "\n".join(lines)