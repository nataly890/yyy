print("=== INICIANDO SISTEMA FINANZAS ===")
print("Cargando...")

# Primero importamos todo
import flet as ft
import random
from datetime import datetime

class SistemaFinanzas:
    def __init__(self, page):
        self.page = page
        self.saldo = 0.0
        self.historial = []
        
        # Crear controles BÁSICOS
        self.texto_titulo = ft.Text("💰 CONTROL FINANCIERO", size=24, weight="bold")
        
        # Campo para monto
        self.campo_monto = ft.TextField(
            label="Monto ($)",
            width=200,
            hint_text="Ej: 1000"
        )
        
        # Selector simple
        self.selector_tipo = ft.Dropdown(
            label="Tipo",
            width=150,
            options=[
                ft.dropdown.Option("Ingreso"),
                ft.dropdown.Option("Gasto"),
            ]
        )
        
        # Texto del saldo
        self.texto_saldo = ft.Text(f"Saldo actual: ${self.saldo:.2f}", size=20)
        
        # Lista para historial
        self.lista_historial = ft.Column(
            spacing=5,
            height=250,
            scroll=ft.ScrollMode.ALWAYS
        )
        
        # Botones SIMPLES
        self.boton_agregar = ft.ElevatedButton(
            "Agregar Transacción",
            on_click=self.agregar_transaccion
        )
        
        self.boton_limpiar = ft.OutlinedButton(
            "Limpiar Todo",
            on_click=self.limpiar_todo
        )
        
        # Construir la interfaz
        self.construir_pagina()
    
    def construir_pagina(self):
        # Fila superior: entrada de datos
        fila_superior = ft.Row([
            self.campo_monto,
            self.selector_tipo,
            self.boton_agregar
        ], alignment=ft.MainAxisAlignment.CENTER)
        
        # Fila media: saldo y botón limpiar
        fila_media = ft.Row([
            self.texto_saldo,
            self.boton_limpiar
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        # Área de historial
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
        
        # Agregar todo a la página
        self.contenido = ft.Column([
            self.texto_titulo,
            ft.Divider(height=20),
            fila_superior,
            ft.Divider(height=10),
            fila_media,
            ft.Divider(height=20),
            area_historial
        ], spacing=10)
        
        self.page.add(self.contenido)
    
    def agregar_transaccion(self, e):
        # Validar que haya datos
        if not self.campo_monto.value or not self.selector_tipo.value:
            self.campo_monto.error_text = "Complete todos los campos"
            self.page.update()
            return
        
        try:
            # Convertir monto a número
            monto = float(self.campo_monto.value)
            tipo = self.selector_tipo.value
            hora = datetime.now().strftime("%H:%M")
            
            # Actualizar saldo
            if tipo == "Ingreso":
                self.saldo += monto
                color_texto = "green"
                simbolo = "[+]"
            else:
                self.saldo -= monto
                color_texto = "red"
                simbolo = "[-]"
            
            # Crear registro
            registro = {
                "id": random.randint(100, 999),
                "monto": monto,
                "tipo": tipo,
                "hora": hora
            }
            self.historial.append(registro)
            
            # Agregar a la lista visual
            texto_transaccion = ft.Text(
                f"{simbolo} ${monto:.2f} ({tipo}) - {hora}",
                color=color_texto
            )
            self.lista_historial.controls.append(texto_transaccion)
            
            # Actualizar saldo display
            self.texto_saldo.value = f"Saldo actual: ${self.saldo:.2f}"
            
            # Limpiar campo
            self.campo_monto.value = ""
            self.campo_monto.error_text = None
            
            # Actualizar página
            self.page.update()
            
            print(f"✅ Transacción agregada: {tipo} ${monto}")
            
        except ValueError:
            self.campo_monto.error_text = "Ingrese un número válido"
            self.page.update()
    
    def limpiar_todo(self, e):
        self.saldo = 0.0
        self.historial.clear()
        self.lista_historial.controls.clear()
        self.texto_saldo.value = f"Saldo actual: ${self.saldo:.2f}"
        self.page.update()
        print("🗑️ Todo limpiado")

# Función principal
def main(page: ft.Page):
    # Configuración MÍNIMA de la página
    page.title = "Sistema Finanzas"
    page.window_width = 550
    page.window_height = 600
    
    # Crear el sistema
    sistema = SistemaFinanzas(page)
    
    print("✅ Aplicación lista!")
    print("🌐 Abre: http://localhost:8888")

# Punto de entrada
if __name__ == "__main__":
    print("🚀 Iniciando aplicación de finanzas...")
    ft.app(target=main, port=8888)
