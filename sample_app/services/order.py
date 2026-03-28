import sqlite3
import smtplib
import logging

# DRY violation: same DB connection pattern repeated
conn = sqlite3.connect("orders.db")


def create_order(customer_id, items, total):
    # Missing type hints, DRY violation (same email logic as user.py)
    if not customer_id or not items:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO orders (customer_id, total) VALUES (?, ?)",
            (customer_id, total),
        )
        conn.commit()
        order_id = cursor.lastrowid
    except Exception:
        return None  # swallowed, no logging

    # Duplicated email logic from user.py
    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.sendmail(
            "no-reply@example.com",
            f"customer_{customer_id}@example.com",
            f"Subject: Order Confirmed\n\nOrder {order_id} placed!",
        )
        server.quit()
    except:
        pass

    return order_id


def get_order(order_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    return cursor.fetchone()


def get_orders_for_customer(customer_id):
    # Same pattern as get_all_users — should be abstracted
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
    return cursor.fetchall()


def cancel_order(order_id, reason):
    # LSP concern: cancellation changes order "state" but there's no contract
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET status = 'cancelled', cancel_reason = ? WHERE id = ?",
            (reason, order_id),
        )
        conn.commit()
    except:
        pass  # swallowed

    # Duplicated email logic (3rd copy)
    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.sendmail(
            "no-reply@example.com",
            "admin@example.com",
            f"Subject: Order Cancelled\n\nOrder {order_id} cancelled: {reason}",
        )
        server.quit()
    except:
        pass


def calculate_total(items):
    # No type hint, magic number
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    if total > 1000:
        total = total * 0.9  # 10% discount — magic number
    return total


def generate_order_report(customer_id):
    # Duplicated report generation pattern from user.py
    orders = get_orders_for_customer(customer_id)
    report = "Order Report\n"
    report += "=" * 20 + "\n"
    for o in orders:
        report += f"Order ID: {o[0]}, Total: {o[2]}\n"
    return report
