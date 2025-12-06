# -*- coding: utf-8 -*-
print("=== APLICACIÓN FINANZAS PROFESIONAL ===")
print("Iniciando sistema...")

import flet as ft
import random
from datetime import datetime

def main(page: ft.Page):
    # Configurar página
    page.title = "💰 Gestor Financiero"
    page.window_width = 1000
    page.window_height = 750
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    
    # Variables de estado
    saldo_total = 0.0
    total_ingresos = 0.0
    total_gastos = 0.0
    historial = []
    
    # ========== COMPONENTES DE LA INTERFAZ ==========
    
    # 1. ENCABEZADO
    header = ft.Container(
        content=ft.Row([
            ft.Icon(name=ft.icons.ACCOUNT_BALANCE, size=40, color=ft.colors.BLUE),
            ft.Column([
                ft.Text("GESTOR FINANCIERO PERSONAL", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("Control total de tus ingresos y gastos", size=16, color=ft.colors.GREY_600)
            ])
        ]),
        padding=ft.padding.only(bottom=20)
    )
    
    # 2. PANEL DE ESTADÍSTICAS
    card_saldo = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("SALDO ACTUAL", size=14, color=ft.colors.GREY_600),
                ft.Text("$0.00", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=200
        )
    )
    
    card_ingresos = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("INGRESOS TOTALES", size=14, color=ft.colors.GREY_600),
                ft.Text("$0.00", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_700)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=180
        )
    )
    
    card_gastos = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("GASTOS TOTALES", size=14, color=ft.colors.GREY_600),
                ft.Text("$0.00", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.RED_700)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=180
        )
    )
    
    card_transacciones = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("TRANSACCIONES", size=14, color=ft.colors.GREY_600),
                ft.Text("0", size=32, weight=ft.FontWeight.BOLD)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=180
        )
    )
    
    panel_estadisticas = ft.Row(
        controls=[card_saldo, card_ingresos, card_gastos, card_transacciones],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )
    
    # 3. FORMULARIO DE TRANSACCIÓN
    titulo_formulario = ft.Text("➕ NUEVA TRANSACCIÓN", size=20, weight=ft.FontWeight.BOLD)
    
    input_monto = ft.TextField(
        label="Monto ($)",
        width=200,
        hint_text="Ej: 1500.50",
        prefix_text="$ ",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    dropdown_categoria = ft.Dropdown(
        label="Categoría",
        width=200,
        options=[
            ft.dropdown.Option("Alimentos"),
            ft.dropdown.Option("Transporte"),
            ft.dropdown.Option("Vivienda"),
            ft.dropdown.Option("Salud"),
            ft.dropdown.Option("Educación"),
            ft.dropdown.Option("Entretenimiento"),
            ft.dropdown.Option("Salario"),
            ft.dropdown.Option("Inversiones"),
            ft.dropdown.Option("Otros")
        ],
        value="Alimentos"
    )
    
    radio_tipo = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="ingreso", label="Ingreso"),
            ft.Radio(value="gasto", label="Gasto"),
        ]),
        value="gasto"
    )
    
    input_descripcion = ft.TextField(
        label="Descripción (opcional)",
        width=400,
        hint_text="Detalles de la transacción..."
    )
    
    btn_agregar = ft.ElevatedButton(
        "Agregar Transacción",
        icon=ft.icons.ADD_CIRCLE_OUTLINE,
        on_click=lambda e: agregar_transaccion(),
        width=200
    )
    
    btn_limpiar = ft.OutlinedButton(
        "Limpiar Todo",
        icon=ft.icons.DELETE,
        on_click=lambda e: limpiar_todo(),
        width=150
    )
    
    formulario = ft.Container(
        content=ft.Column([
            titulo_formulario,
            ft.Divider(height=10),
            ft.Row([input_monto, dropdown_categoria]),
            ft.Container(height=10),
            ft.Row([
                ft.Text("Tipo:", size=16),
                radio_tipo
            ]),
            ft.Container(height=10),
            input_descripcion,
            ft.Container(height=15),
            ft.Row([btn_agregar, btn_limpiar], alignment=ft.MainAxisAlignment.CENTER)
        ]),
        padding=25,
        border=ft.border.all(1, ft.colors.GREY_300),
        border_radius=10,
        bgcolor=ft.colors.GREY_50
    )
    
    # 4. HISTORIAL DE TRANSACCIONES
    titulo_historial = ft.Text("📋 HISTORIAL DE TRANSACCIONES", size=20, weight=ft.FontWeight.BOLD)
    
    lista_historial = ft.ListView(
        expand=True,
        spacing=10,
        padding=10
    )
    
    panel_historial = ft.Container(
        content=ft.Column([
            titulo_historial,
            ft.Divider(height=10),
            ft.Container(
                content=lista_historial,
                height=250,
                border=ft.border.all(1, ft.colors.GREY_300),
                border_radius=10,
                padding=15
            )
        ])
    )
    
    # 5. FUNCIONES
    def actualizar_estadisticas():
        nonlocal saldo_total, total_ingresos, total_gastos
        
        # Actualizar tarjetas
        card_saldo.content.content.controls[1].value = f"${saldo_total:,.2f}"
        card_ingresos.content.content.controls[1].value = f"${total_ingresos:,.2f}"
        card_gastos.content.content.controls[1].value = f"${total_gastos:,.2f}"
        card_transacciones.content.content.controls[1].value = str(len(historial))
        
        # Color del saldo según valor
        if saldo_total >= 0:
            card_saldo.content.content.controls[1].color = ft.colors.GREEN_700
        else:
            card_saldo.content.content.controls[1].color = ft.colors.RED_700
        
        page.update()
    
    def agregar_transaccion():
        nonlocal saldo_total, total_ingresos, total_gastos
        
        if not input_monto.value:
            input_monto.error_text = "Ingrese un monto"
            page.update()
            return
        
        try:
            monto = float(input_monto.value)
            tipo = radio_tipo.value
            categoria = dropdown_categoria.value
            descripcion = input_descripcion.value
            fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            trans_id = random.randint(1000, 9999)
            
            # Actualizar valores
            if tipo == "ingreso":
                saldo_total += monto
                total_ingresos += monto
                color_item = ft.colors.GREEN
                icono_item = ft.icons.ARROW_UPWARD
                texto_tipo = "INGRESO"
            else:
                saldo_total -= monto
                total_gastos += monto
                color_item = ft.colors.RED
                icono_item = ft.icons.ARROW_DOWNWARD
                texto_tipo = "GASTO"
            
            # Crear registro
            registro = {
                "id": trans_id,
                "monto": monto,
                "tipo": tipo,
                "categoria": categoria,
                "descripcion": descripcion,
                "fecha": fecha_hora
            }
            historial.append(registro)
            
            # Agregar a la lista visual
            item = ft.Card(
                content=ft.ListTile(
                    leading=ft.Icon(icono_item, color=color_item),
                    title=ft.Text(f"${monto:,.2f} - {categoria}"),
                    subtitle=ft.Text(f"{texto_tipo} | {fecha_hora}"),
                    trailing=ft.Text(f"#{trans_id}")
                )
            )
            
            lista_historial.controls.insert(0, item)
            
            # Actualizar estadísticas
            actualizar_estadisticas()
            
            # Limpiar formulario
            input_monto.value = ""
            input_descripcion.value = ""
            input_monto.error_text = None
            
            print(f"Transacción #{trans_id} agregada: {texto_tipo} ${monto}")
            
        except ValueError:
            input_monto.error_text = "Ingrese un número válido"
            page.update()
    
    def limpiar_todo():
        nonlocal saldo_total, total_ingresos, total_gastos
        
        # Resetear valores
        saldo_total = 0.0
        total_ingresos = 0.0
        total_gastos = 0.0
        historial.clear()
        
        # Limpiar lista visual
        lista_historial.controls.clear()
        
        # Actualizar interfaz
        actualizar_estadisticas()
        
        # Limpiar campos
        input_monto.value = ""
        input_descripcion.value = ""
        input_monto.error_text = None
        
        print("Historial limpiado")
    
    # 6. CONSTRUIR PÁGINA COMPLETA
    pagina_completa = ft.Column([
        header,
        panel_estadisticas,
        ft.Divider(height=30),
        formulario,
        ft.Divider(height=30),
        panel_historial,
        ft.Divider(height=20),
        ft.Text("© 2024 Gestor Financiero v1.0 | Desarrollado con Flet", 
               size=12, color=ft.colors.GREY_500, text_align=ft.TextAlign.CENTER)
    ], spacing=15)
    
    # Agregar todo a la página
    page.add(pagina_completa)
    
    print("✅ Aplicación lista en http://localhost:8888")

# Iniciar aplicación
if __name__ == "__main__":
    ft.app(target=main, port=8888)
