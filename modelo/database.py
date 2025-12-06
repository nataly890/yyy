import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path='modelo/finanzas.db'):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initialize the database with tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create balance table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS balance (
                id INTEGER PRIMARY KEY,
                amount REAL NOT NULL DEFAULT 0.0
            )
        ''')

        # Create transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Insert initial balance if not exists
        cursor.execute('INSERT OR IGNORE INTO balance (id, amount) VALUES (1, 0.0)')

        conn.commit()
        conn.close()

    def get_balance(self):
        """Get current balance."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT amount FROM balance WHERE id = 1')
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else 0.0

    def update_balance(self, amount, transaction_type):
        """Update balance based on transaction."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        current_balance = self.get_balance()
        if transaction_type == 'Ingreso':
            new_balance = current_balance + amount
        else:
            new_balance = current_balance - amount

        cursor.execute('UPDATE balance SET amount = ? WHERE id = 1', (new_balance,))
        conn.commit()
        conn.close()
        return new_balance

    def add_transaction(self, amount, transaction_type):
        """Add a new transaction."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO transactions (amount, type) VALUES (?, ?)', (amount, transaction_type))
        conn.commit()
        conn.close()

    def get_transactions(self):
        """Get all transactions."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, amount, type, timestamp FROM transactions ORDER BY timestamp DESC')
        transactions = cursor.fetchall()
        conn.close()
        return transactions

    def clear_all(self):
        """Clear all data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('UPDATE balance SET amount = 0.0 WHERE id = 1')
        cursor.execute('DELETE FROM transactions')
        conn.commit()
        conn.close()
