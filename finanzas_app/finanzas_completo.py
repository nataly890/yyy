print("=== SISTEMA FINANZAS COMPLETO ===")
print("Cargando aplicación mejorada...")

import flet as ft
import random
from datetime import datetime

class SistemaFinanzasMejorado:
    def __init__(self, page):
        self.page = page
        self.saldo = 0.0
        self.ingresos_totales = 0.0
        self.gastos_totales = 0.0
        self.transacciones = []
        
        # ========== TÍTULO Y ENCABEZADO ==========
        self.titulo = ft.Text("💰 GESTIÓN FINANCIERA PERSONAL", 
                             size=28, 
                             weight=ft.FontWeight.BOLD,
                             text_align=ft.TextAlign.CENTER)
        
        self.subtitulo = ft.Text("Controla tus ingresos y gastos fácilmente",
                                size=16,
                                color=ft.colors.GREY_600,
                                text_align=ft.TextAlign.CENTER)
        
        # ========== PANEL DE ESTADÍSTICAS ==========
        self.tarjeta_saldo = ft.Container(
            content=ft.Column([
                ft.Text("SALDO ACTUAL", size=14, color=ft.colors.GREY_500),
                ft.Text("$0.00", size=36, weight=ft.FontWeight.BOLD)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            bgcolor=ft.colors.BLUE_50,
            border_radius=10,
            width=180
        )
        
        self.tarjeta_ingresos = ft.Container(
            content=ft.Column([
                ft.Text("INGRESOS", size=14, color=ft.colors.GREY_500),
                ft.Text("$0.00", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor=ft.colors.GREEN_50,
            border_radius=10,
            width=150
        )
        
        self.tarjeta_gastos = ft.Container(
            content=ft.Column([
                ft.Text("GASTOS", size=14, color=ft.colors.GREY_500),
                ft.Text("$0.00", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.RED)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor=ft.colors.RED_50,
            border_radius=10,
            width=150
        )
        
        self.tarjeta_total = ft.Container(
            content=ft.Column([
                ft.Text("TRANSACCIONES", size=14, color=ft.colors.GREY_500),
                ft.Text("0", size=24, weight=ft.FontWeight.BOLD)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            bgcolor=ft.colors.PURPLE_50,
            border_radius=10,
            width=150
        )
        
        # ========== FORMULARIO DE TRANSACCIÓN ==========
        self.texto_formulario = ft.Text("➕ NUEVA TRANSACCIÓN", 
                                       size=18, 
                                       weight=ft.FontWeight.BOLD)
        
        # Campo monto
        self.campo_monto = ft.TextField(
            label="Monto ($)",
            width=180,
            hint_text="Ej: 1500.50",
            border_color=ft.colors.BLUE_400,
            prefix_text="$",
            keyboard_type=ft.KeyboardType.NUMBER
        )
        
        # Selector de categoría
        self.selector_categoria = ft.Dropdown(
            label="Categoría",
            width=180,
            options=[
                ft.dropdown.Option("🏠 Vivienda"),
                ft.dropdown.Option("🍔 Alimentos"),
                ft.dropdown.Option("🚗 Transporte"),
                ft.dropdown.Option("💼 Trabajo"),
                ft.dropdown.Option("🎮 Entretenimiento"),
                ft.dropdown.Option("🏥 Salud"),
                ft.dropdown.Option("👗 Ropa"),
                ft.dropdown.Option("📚 Educación"),
                ft.dropdown.Option("💰 Salario"),
                ft.dropdown.Option("📱 Otros")
            ],
            value="🍔 Alimentos"
        )
        
        # Selector de tipo con íconos
        self.selector_tipo = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value="ingreso", label="Ingreso"),
                ft.Radio(value="gasto", label="Gasto"),
            ]),
            value="gasto"
        )
        
        # Campo descripción
        self.campo_descripcion = ft.TextField(
            label="Descripción (opcional)",
            width=350,
            hint_text="Ej: Supermercado mensual, Pago de salario...",
            multiline=True,
            min_lines=2,
            max_lines=3
        )
        
        # Botones
        self.boton_ingreso = ft.ElevatedButton(
            "➕ Agregar Ingreso",
            on_click=lambda e: self.agregar_transaccion("ingreso"),
            icon=ft.icons.ADD,
            bgcolor=ft.colors.GREEN,
            color=ft.colors.WHITE,
            width=180
        )
        
        self.boton_gasto = ft.ElevatedButton(
            "➖ Agregar Gasto",
            on_click=lambda e: self.agregar_transaccion("gasto"),
            icon=ft.icons.REMOVE,
            bgcolor=ft.colors.RED,
            color=ft.colors.WHITE,
            width=180
        )
        
        self.boton_limpiar = ft.OutlinedButton(
            "🗑️ Limpiar Historial",
            on_click=self.limpiar_todo,
            icon=ft.icons.DELETE,
            width=180
        )
        
        # ========== HISTORIAL DE TRANSACCIONES ==========
        self.texto_historial = ft.Text("📋 HISTORIAL DE TRANSACCIONES", 
                                      size=18, 
                                      weight=ft.FontWeight.BOLD)
        
        # Lista de transacciones
        self.lista_transacciones = ft.ListView(
            expand=True,
            spacing=10,
            padding=10
        )
        
        # ========== PIE DE PÁGINA ==========
        self.pie_pagina = ft.Text("© 2024 Sistema Financiero Personal v1.0 | Total transacciones: 0",
                                 size=12,
                                 color=ft.colors.GREY_500,
                                 text_align=ft.TextAlign.CENTER)
        
        # Construir la interfaz
        self.construir_interfaz()
    
    def construir_interfaz(self):
        # Fila 1: Encabezado
        encabezado = ft.Column([
            self.titulo,
            self.subtitulo
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        # Fila 2: Panel de estadísticas
        panel_estadisticas = ft.Row([
            self.tarjeta_saldo,
            self.tarjeta_ingresos,
            self.tarjeta_gastos,
            self.tarjeta_total
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY)
        
        # Fila 3: Formulario
        panel_formulario = ft.Container(
            content=ft.Column([
                self.texto_formulario,
                ft.Divider(height=10),
                ft.Row([
                    ft.Column([
                        ft.Text("Monto:", size=14),
                        self.campo_monto
                    ]),
                    ft.Column([
                        ft.Text("Categoría:", size=14),
                        self.selector_categoria
                    ]),
                    ft.Column([
                        ft.Text("Tipo:", size=14),
                        self.selector_tipo
                    ])
                ]),
                ft.Container(height=10),
                self.campo_descripcion,
                ft.Container(height=15),
                ft.Row([
                    self.boton_ingreso,
                    self.boton_gasto,
                    self.boton_limpiar
                ],
                alignment=ft.MainAxisAlignment.CENTER)
            ]),
            padding=20,
            border=ft.border.all(1, ft.colors.GREY_300),
            border_radius=10,
            bgcolor=ft.colors.GREY_50
        )
        
        # Fila 4: Historial
        panel_historial = ft.Container(
            content=ft.Column([
                self.texto_historial,
                ft.Divider(height=10),
                ft.Container(
                    content=self.lista_transacciones,
                    height=300,
                    border=ft.border.all(1, ft.colors.GREY_300),
                    border_radius=10,
                    padding=10
                )
            ])
        )
        
        # Contenedor principal
        self.contenido = ft.Column([
            encabezado,
            ft.Divider(height=30),
            panel_estadisticas,
            ft.Divider(height=30),
            panel_formulario,
            ft.Divider(height=30),
            panel_historial,
            ft.Divider(height=20),
            self.pie_pagina
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=15)
        
        self.page.add(self.contenido)
    
    def agregar_transaccion(self, tipo_transaccion):
        # Validar campos
        if not self.campo_monto.value:
            self.campo_monto.error_text = "Ingrese un monto"
            self.page.update()
            return
        
        try:
            # Obtener datos
            monto = float(self.campo_monto.value)
            categoria = self.selector_categoria.value
            descripcion = self.campo_descripcion.value
            fecha_hora = datetime.now().strftime("%d/%m %H:%M")
            transaccion_id = random.randint(1000, 9999)
            
            # Actualizar estadísticas
            if tipo_transaccion == "ingreso":
                self.saldo += monto
                self.ingresos_totales += monto
                color = ft.colors.GREEN
                icono = ft.icons.ARROW_UPWARD
                texto_tipo = "INGRESO"
            else:
                self.saldo -= monto
                self.gastos_totales += monto
                color = ft.colors.RED
                icono = ft.icons.ARROW_DOWNWARD
                texto_tipo = "GASTO"
            
            # Crear transacción
            transaccion = {
                "id": transaccion_id,
                "monto": monto,
                "tipo": tipo_transaccion,
                "categoria": categoria,
                "descripcion": descripcion,
                "fecha": fecha_hora
            }
            self.transacciones.append(transaccion)
            
            # Actualizar tarjetas de estadísticas
            self.actualizar_estadisticas()
            
            # Agregar a historial visual
            self.agregar_al_historial(transaccion, color, icono, texto_tipo)
            
            # Limpiar formulario
            self.campo_monto.value = ""
            self.campo_descripcion.value = ""
            self.campo_monto.error_text = None
            self.page.update()
            
            print(f"✅ {texto_tipo} #{transaccion_id}: ${monto:.2f}")
            
        except ValueError:
            self.campo_monto.error_text = "Ingrese un número válido"
            self.page.update()
    
    def actualizar_estadisticas(self):
        # Actualizar todas las tarjetas
        self.tarjeta_saldo.content.controls[1].value = f"${self.saldo:,.2f}"
        self.tarjeta_ingresos.content.controls[1].value = f"${self.ingresos_totales:,.2f}"
        self.tarjeta_gastos.content.controls[1].value = f"${self.gastos_totales:,.2f}"
        self.tarjeta_total.content.controls[1].value = str(len(self.transacciones))
        
        # Color del saldo (verde si positivo, rojo si negativo)
        if self.saldo >= 0:
            self.tarjeta_saldo.content.controls[1].color = ft.colors.GREEN
        else:
            self.tarjeta_saldo.content.controls[1].color = ft.colors.RED
        
        # Actualizar pie de página
        self.pie_pagina.value = f"© 2024 Sistema Financiero Personal v1.0 | Total transacciones: {len(self.transacciones)}"
    
    def agregar_al_historial(self, transaccion, color, icono, texto_tipo):
        # Crear tarjeta para la transacción
        tarjeta_transaccion = ft.Card(
            content=ft.Container(
                content=ft.ListTile(
                    leading=ft.Icon(icono, color=color),
                    title=ft.Text(f"${transaccion['monto']:,.2f} - {transaccion['categoria']}"),
                    subtitle=ft.Text(f"{texto_tipo} | {transaccion['fecha']} | ID: #{transaccion['id']}"),
                    trailing=ft.Icon(ft.icons.CHECK_CIRCLE, color=color),
                ),
                padding=5
            )
        )
        
        # Agregar al inicio de la lista
        self.lista_transacciones.controls.insert(0, tarjeta_transaccion)
    
    def limpiar_todo(self, e):
        # Resetear todo
        self.saldo = 0.0
        self.ingresos_totales = 0.0
        self.gastos_totales = 0.0
        self.transacciones.clear()
        self.lista_transacciones.controls.clear()
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()
        
        # Limpiar campos
        self.campo_monto.value = ""
        self.campo_descripcion.value = ""
        self.campo_monto.error_text = None
        
        self.page.update()
        print("🗑️ Todo el historial ha sido limpiado")

def main(page: ft.Page):
    # Configuración de la página
    page.title = "💰 Sistema Financiero Personal"
    page.window_width = 1000
    page.window_height = 850
    page.window_resizable = True
    page.padding = 25
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Crear la aplicación
    app = SistemaFinanzasMejorado(page)
    
    print("✅ Aplicación mejorada cargada exitosamente!")
    print("🌐 Disponible en: http://localhost:8888")

if __name__ == "__main__":
    print("🚀 Iniciando Sistema Financiero Personal...")
    ft.app(target=main, port=8888)
