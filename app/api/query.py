from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.query import QueryRequest, QueryResponse


router = APIRouter(
    prefix="/api/v1",
    tags=["NL2SQL"]
)


@router.post("/query", response_model=QueryResponse)
def natural_language_query(
    request: QueryRequest,
    db: Session = Depends(get_db)
):
    question = request.question.lower()

    # Top 5 products by sales
    if (
        "top 5" in question
        and "product" in question
        and "sales" in question
    ):
        sql = """
        SELECT
            p.product_name,
            SUM(oi.sales) AS total_sales
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_sales DESC
        LIMIT 5
        """

    # Top 5 products by profit
    elif (
        "top 5" in question
        and "product" in question
        and "profit" in question
    ):
        sql = """
        SELECT
            p.product_name,
            SUM(oi.profit_per_order) AS total_profit
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_profit DESC
        LIMIT 5
        """

    # Sales by customer segment
    elif (
        "customer segment" in question
        and "sales" in question
    ):
        sql = """
        SELECT
            c.customer_segment,
            SUM(oi.sales) AS total_sales
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY c.customer_segment
        ORDER BY total_sales DESC
        """

    # Average shipping time by shipping mode
    elif "shipping mode" in question:
        sql = """
        SELECT
            o.shipping_mode,
            AVG(o.days_for_shipping_real) AS average_shipping_days
        FROM orders o
        GROUP BY o.shipping_mode
        ORDER BY average_shipping_days DESC
        """

    # Count late orders
    elif (
        "late" in question
        and "order" in question
    ):
        sql = """
        SELECT
            COUNT(*) AS late_orders
        FROM orders
        WHERE late_delivery_risk = 1
        """

    else:
        raise HTTPException(
            status_code=400,
            detail="This question is not supported yet."
        )

    result = db.execute(text(sql))

    columns = result.keys()

    rows = [
        dict(zip(columns, row))
        for row in result.fetchall()
    ]

    return {
        "question": request.question,
        "sql": sql.strip(),
        "results": rows
    }