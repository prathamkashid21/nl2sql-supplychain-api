import pandas as pd
from sqlalchemy.orm import Session

from app.database.db import engine, Base
from app.models.customer import Customer
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem


CSV_FILE = "data/DataCoSupplyChainDataset.csv"


def load_data():
    print("Reading dataset...")

    df = pd.read_csv(
        CSV_FILE,
        encoding="latin1"
    )

    print(f"Dataset loaded: {len(df)} rows")

    # Create tables
    Base.metadata.create_all(bind=engine)

    session = Session(engine)

    try:
        # --------------------------------------------------
        # CUSTOMERS
        # --------------------------------------------------

        print("Loading customers...")

        customers = (
            df[
                [
                    "Customer Id",
                    "Customer Segment",
                    "Customer City",
                    "Customer State",
                    "Customer Country",
                    "Customer Zipcode",
                ]
            ]
            .drop_duplicates(subset=["Customer Id"])
        )

        for _, row in customers.iterrows():
            session.add(
                Customer(
                    customer_id=int(row["Customer Id"]),
                    customer_segment=row["Customer Segment"],
                    city=row["Customer City"],
                    state=row["Customer State"],
                    country=row["Customer Country"],
                    zipcode=(
                        int(row["Customer Zipcode"])
                        if pd.notna(row["Customer Zipcode"])
                        else None
                    ),
                )
            )

        session.commit()

        print(f"Customers loaded: {len(customers)}")

        # --------------------------------------------------
        # PRODUCTS
        # --------------------------------------------------

        print("Loading products...")

        products = (
            df[
                [
                    "Product Card Id",
                    "Product Name",
                    "Category Id",
                    "Category Name",
                    "Department Id",
                    "Department Name",
                    "Product Price",
                ]
            ]
            .drop_duplicates(subset=["Product Card Id"])
        )

        for _, row in products.iterrows():
            session.add(
                Product(
                    product_id=int(row["Product Card Id"]),
                    product_name=row["Product Name"],
                    category_id=int(row["Category Id"]),
                    category_name=row["Category Name"],
                    department_id=int(row["Department Id"]),
                    department_name=row["Department Name"],
                    product_price=float(row["Product Price"]),
                )
            )

        session.commit()

        print(f"Products loaded: {len(products)}")

        # --------------------------------------------------
        # ORDERS
        # --------------------------------------------------

        print("Loading orders...")

        orders = (
            df[
                [
                    "Order Id",
                    "Order Customer Id",
                    "order date (DateOrders)",
                    "Order Status",
                    "Market",
                    "Order City",
                    "Order State",
                    "Order Country",
                    "Order Region",
                    "Shipping Mode",
                    "shipping date (DateOrders)",
                    "Days for shipping (real)",
                    "Days for shipment (scheduled)",
                    "Delivery Status",
                    "Late_delivery_risk",
                    "Order Zipcode",
                ]
            ]
            .drop_duplicates(subset=["Order Id"])
        )

        for _, row in orders.iterrows():
            session.add(
                Order(
                    order_id=int(row["Order Id"]),
                    customer_id=int(row["Order Customer Id"]),
                    order_date=pd.to_datetime(
                        row["order date (DateOrders)"]
                    ),
                    order_status=row["Order Status"],
                    market=row["Market"],
                    order_city=row["Order City"],
                    order_state=row["Order State"],
                    order_country=row["Order Country"],
                    order_region=row["Order Region"],
                    shipping_mode=row["Shipping Mode"],
                    shipping_date=pd.to_datetime(
                        row["shipping date (DateOrders)"]
                    ),
                    days_for_shipping_real=int(
                        row["Days for shipping (real)"]
                    ),
                    days_for_shipment_scheduled=int(
                        row["Days for shipment (scheduled)"]
                    ),
                    delivery_status=row["Delivery Status"],
                    late_delivery_risk=int(
                        row["Late_delivery_risk"]
                    ),
                    order_zipcode=(
                        float(row["Order Zipcode"])
                        if pd.notna(row["Order Zipcode"])
                        else None
                    ),
                )
            )

        session.commit()

        print(f"Orders loaded: {len(orders)}")

        # --------------------------------------------------
        # ORDER ITEMS
        # --------------------------------------------------

        print("Loading order items...")

        order_items = df[
            [
                "Order Item Id",
                "Order Id",
                "Product Card Id",
                "Order Item Quantity",
                "Order Item Product Price",
                "Order Item Discount",
                "Order Item Discount Rate",
                "Sales",
                "Order Item Total",
                "Order Item Profit Ratio",
                "Order Profit Per Order",
                "Benefit per order",
            ]
        ]

        for _, row in order_items.iterrows():
            session.add(
                OrderItem(
                    order_item_id=int(row["Order Item Id"]),
                    order_id=int(row["Order Id"]),
                    product_id=int(row["Product Card Id"]),
                    quantity=int(row["Order Item Quantity"]),
                    product_price=float(
                        row["Order Item Product Price"]
                    ),
                    discount=float(row["Order Item Discount"]),
                    discount_rate=float(
                        row["Order Item Discount Rate"]
                    ),
                    sales=float(row["Sales"]),
                    total=float(row["Order Item Total"]),
                    profit_ratio=float(
                        row["Order Item Profit Ratio"]
                    ),
                    profit_per_order=float(
                        row["Order Profit Per Order"]
                    ),
                    benefit_per_order=float(
                        row["Benefit per order"]
                    ),
                )
            )

        session.commit()

        print(f"Order items loaded: {len(order_items)}")

        print("\n================================")
        print("DATABASE LOADING COMPLETE")
        print("================================")

    except Exception as e:
        session.rollback()
        print("\nERROR:", e)
        raise

    finally:
        session.close()


if __name__ == "__main__":
    load_data()