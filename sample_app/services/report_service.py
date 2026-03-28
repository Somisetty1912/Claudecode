"""
Centralized report generation service.
Consolidates report generation logic from user.py and order.py.
Provides unified report generation interface.
"""

from typing import List, Dict, Any, Tuple
from datetime import datetime
from ..utils import formatters, constants


class ReportGenerator:
    """Unified report generator for users and orders."""

    @staticmethod
    def generate_user_report(users: List[Tuple]) -> str:
        """
        Generate user report from user tuples.

        Args:
            users: List of user tuples (name, email, id, role)

        Returns:
            Formatted user report string

        Example:
            users = [('John', 'john@example.com', 1, 'admin')]
            report = ReportGenerator.generate_user_report(users)
        """
        report = formatters.format_report_header("User Report")

        admin_count = 0
        regular_count = 0

        for user in users:
            name, email, role = user[0], user[1], user[3]
            report += formatters.format_user_report_line(name, email, role)

            if role == constants.ROLE_ADMIN:
                admin_count += 1
            else:
                regular_count += 1

        report += "\n"
        report += formatters.format_statistics("Admins", admin_count)
        report += formatters.format_statistics("Regular", regular_count)
        report += formatters.format_report_line("Generated", str(datetime.now()))

        return report

    @staticmethod
    def generate_order_report(orders: List[Tuple]) -> str:
        """
        Generate order report from order tuples.

        Args:
            orders: List of order tuples (id, customer_id, total)

        Returns:
            Formatted order report string

        Example:
            orders = [(1, 100, 99.99)]
            report = ReportGenerator.generate_order_report(orders)
        """
        report = formatters.format_report_header("Order Report")

        total_revenue = 0.0
        order_count = 0

        for order in orders:
            order_id, total = order[0], order[2]
            report += formatters.format_order_report_line(order_id, total)
            total_revenue += total
            order_count += 1

        report += "\n"
        report += formatters.format_statistics("Total Orders", order_count)
        report += formatters.format_report_line("Total Revenue", f"${total_revenue:.2f}")
        report += formatters.format_report_line("Generated", str(datetime.now()))

        return report

    @staticmethod
    def generate_custom_report(
        title: str,
        rows: List[Dict[str, Any]],
        columns: List[str],
    ) -> str:
        """
        Generate custom report with specified columns.

        Args:
            title: Report title
            rows: List of data rows
            columns: Column names to include

        Returns:
            Formatted report string

        Example:
            rows = [{'name': 'John', 'status': 'active'}]
            report = ReportGenerator.generate_custom_report('Users', rows, ['name', 'status'])
        """
        report = formatters.format_report_header(title)

        for row in rows:
            row_text = ", ".join(
                f"{col}: {row.get(col, 'N/A')}"
                for col in columns
            )
            report += row_text + "\n"

        report += "\n"
        report += formatters.format_report_line("Generated", str(datetime.now()))

        return report


# Global report generator instance
report_generator = ReportGenerator()
