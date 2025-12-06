import flet as ft

class UI:
    def __init__(self, page, controller):
        self.page = page
        self.controller = controller
        self.create_components()

    def create_components(self):
        """Create all UI components."""
        # Title
        self.texto_titulo = ft.Text("💰 CONTROL FINANCIERO", size=24, weight="bold")

        # Amount field
        self.campo_monto = ft.TextField(
            label="Monto ($)",
            width=200,
            hint_text="Ej: 1000"
        )

        # Type selector
        self.selector_tipo = ft.Dropdown(
            label="Tipo",
            width=150,
            options=[
                ft.dropdown.Option("Ingreso"),
                ft.dropdown.Option("Gasto"),
            ]
        )

        # Balance display
        self.texto_saldo = ft.Text(f"Saldo actual: ${self.controller.get_balance():.2f}", size=20)

        # Transaction history list
        self.lista_historial = ft.Column(
            spacing=5,
            height=250,
            scroll=ft.ScrollMode.ALWAYS
        )

        # Buttons
        self.boton_agregar = ft.ElevatedButton(
            "Agregar Transacción",
            on_click=self.controller.add_transaction
        )

        self.boton_limpiar = ft.OutlinedButton(
            "Limpiar Todo",
            on_click=self.controller.clear_all
        )

    def build_layout(self):
        """Build the page layout."""
        # Top row: input fields
        fila_superior = ft.Row([
            self.campo_monto,
            self.selector_tipo,
            self.boton_agregar
        ], alignment=ft.MainAxisAlignment.CENTER)

        # Middle row: balance and clear button
        fila_media = ft.Row([
            self.texto_saldo,
            self.boton_limpiar
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        # History area
        area_historial = ft.Container(
            content=ft.Column([
                ft.Text("📋 Historial de Transacciones:", size=18),
                ft.Container(
                    content=self.lista_historial,
                    border=ft.border.all(1),
                    padding=10,
                    border_radius=5
                )
            ])
        )

        # Main content
        self.contenido = ft.Column([
            self.texto_titulo,
            ft.Divider(height=20),
            fila_superior,
            ft.Divider(height=10),
            fila_media,
            ft.Divider(height=20),
            area_historial
        ], spacing=10)

        return self.contenido

    def update_balance_display(self, balance):
        """Update the balance text."""
        self.texto_saldo.value = f"Saldo actual: ${balance:.2f}"
        self.page.update()

    def add_transaction_to_list(self, amount, transaction_type, timestamp):
        """Add a transaction to the history list."""
        if transaction_type == "Ingreso":
            color_texto = "green"
            simbolo = "[+]"
        else:
            color_texto = "red"
            simbolo = "[-]"

        texto_transaccion = ft.Text(
            f"{simbolo} ${amount:.2f} ({transaction_type}) - {timestamp}",
            color=color_texto
        )
        self.lista_historial.controls.append(texto_transaccion)
        self.page.update()

    def clear_history_list(self):
        """Clear the transaction history list."""
        self.lista_historial.controls.clear()
        self.page.update()

    def get_input_values(self):
        """Get current input values."""
        return self.campo_monto.value, self.selector_tipo.value

    def clear_inputs(self):
        """Clear input fields."""
        self.campo_monto.value = ""
        self.campo_monto.error_text = None
        self.page.update()

    def set_error(self, message):
        """Set error message on amount field."""
        self.campo_monto.error_text = message
        self.page.update()
