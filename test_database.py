from sqlalchemy import text
from app.database.db import engine


def test_database():

    with engine.connect() as connection:

        # Test 1: Count customers
        result = connection.execute(
            text("SELECT COUNT(*) FROM customers")
        )

        print("Customers:", result.scalar())

        # Test 2: Count orders
        result = connection.execute(
            text("SELECT COUNT(*) FROM orders")
        )

        print("Orders:", result.scalar())

        # Test 3: Count order items
        result = connection.execute(
            text("SELECT COUNT(*) FROM order_items")
        )

        print("Order Items:", result.scalar())

        # Test 4: Count products
        result = connection.execute(
            text("SELECT COUNT(*) FROM products")
        )

        print("Products:", result.scalar())

        # Test 5: Top 5 products by sales
        result = connection.execute(
            text("""
                SELECT
                    p.product_name,
                    SUM(oi.sales) AS total_sales
                FROM order_items oi
                JOIN products p
                    ON oi.product_id = p.product_id
                GROUP BY p.product_name
                ORDER BY total_sales DESC
                LIMIT 5
            """)
        )

        print("\nTop 5 Products by Sales:")

        for row in result:
            print(row)


if __name__ == "__main__":
    test_database()