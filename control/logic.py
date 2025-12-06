from modelo.database import Database
from vista.ui import UI
from datetime import datetime

class Controller:
    def __init__(self, page):
        self.page = page
        self.db = Database()
        self.ui = UI(page, self)
        self.setup_page()

    def setup_page(self):
        """Setup the page with UI and load existing data."""
        self.page.title = "Sistema Finanzas"
        self.page.window_width = 550
        self.page.window_height = 600

        # Load existing transactions
        self.load_transactions()

        # Add UI to page
        self.page.add(self.ui.build_layout())

    def get_balance(self):
        """Get current balance from database."""
        return self.db.get_balance()

    def add_transaction(self, e):
        """Handle adding a new transaction."""
        amount_str, transaction_type = self.ui.get_input_values()

        # Validate inputs
        if not amount_str or not transaction_type:
            self.ui.set_error("Complete todos los campos")
            return

        try:
            amount = float(amount_str)

            # Update database
            new_balance = self.db.update_balance(amount, transaction_type)
            self.db.add_transaction(amount, transaction_type)

            # Update UI
            self.ui.update_balance_display(new_balance)
            timestamp = datetime.now().strftime("%H:%M")
            self.ui.add_transaction_to_list(amount, transaction_type, timestamp)
            self.ui.clear_inputs()

            print(f"✅ Transacción agregada: {transaction_type} ${amount}")

        except ValueError:
            self.ui.set_error("Ingrese un número válido")

    def load_transactions(self):
        """Load existing transactions from database."""
        transactions = self.db.get_transactions()
        for transaction in transactions:
            _, amount, transaction_type, timestamp = transaction
            # Convert timestamp to time format
            dt = datetime.fromisoformat(timestamp)
            time_str = dt.strftime("%H:%M")
            self.ui.add_transaction_to_list(amount, transaction_type, time_str)

    def clear_all(self, e):
        """Handle clearing all data."""
        self.db.clear_all()
        self.ui.update_balance_display(0.0)
        self.ui.clear_history_list()
        print("🗑️ Todo limpiado")
