"""
Centralized database access layer.
Consolidates all database operations and connection management.
Eliminates DRY violations in SQLite queries.
"""

import sqlite3
from typing import Optional, Tuple, List, Any
import logging

logger = logging.getLogger(__name__)


class DatabaseConnection:
    """Centralized database connection manager."""

    def __init__(self, database_file: str):
        """
        Initialize database connection.

        Args:
            database_file: Path to SQLite database file
        """
        self.database_file = database_file
        self.conn = None

    def connect(self) -> sqlite3.Connection:
        """
        Establish database connection.

        Returns:
            SQLite connection object
        """
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(self.database_file)
                logger.debug(f"Connected to database: {self.database_file}")
            except sqlite3.Error as e:
                logger.error(f"Database connection error: {e}")
                raise
        return self.conn

    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            try:
                self.conn.close()
                self.conn = None
                logger.debug("Database connection closed")
            except sqlite3.Error as e:
                logger.error(f"Error closing database: {e}")

    def execute(self, query: str, params: Tuple = ()) -> Optional[Any]:
        """
        Execute a database query.

        Args:
            query: SQL query string
            params: Query parameters

        Returns:
            Cursor object for SELECT queries, None for INSERT/UPDATE/DELETE

        Raises:
            sqlite3.Error: If query execution fails
        """
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor
        except sqlite3.Error as e:
            logger.error(f"Query execution error: {e}")
            raise

    def execute_and_commit(self, query: str, params: Tuple = ()) -> Optional[int]:
        """
        Execute a query and commit changes.

        Args:
            query: SQL query string
            params: Query parameters

        Returns:
            Last inserted row ID for INSERT queries, or None

        Raises:
            sqlite3.Error: If query execution fails
        """
        try:
            cursor = self.execute(query, params)
            self.conn.commit()
            logger.debug(f"Query committed: {query[:50]}...")
            return cursor.lastrowid if cursor else None
        except sqlite3.Error as e:
            if self.conn:
                self.conn.rollback()
            logger.error(f"Commit error: {e}")
            raise

    def fetch_one(self, query: str, params: Tuple = ()) -> Optional[Tuple]:
        """
        Fetch single row from database.

        Args:
            query: SQL query string
            params: Query parameters

        Returns:
            Single row tuple or None
        """
        try:
            cursor = self.execute(query, params)
            return cursor.fetchone()
        except sqlite3.Error as e:
            logger.error(f"Fetch one error: {e}")
            raise

    def fetch_all(self, query: str, params: Tuple = ()) -> List[Tuple]:
        """
        Fetch all rows from database.

        Args:
            query: SQL query string
            params: Query parameters

        Returns:
            List of row tuples
        """
        try:
            cursor = self.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Fetch all error: {e}")
            raise


# Database connection instances
user_db = DatabaseConnection("users.db")
order_db = DatabaseConnection("orders.db")
