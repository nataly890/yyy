# -*- coding: utf-8 -*-
print("=== SISTEMA FINANZAS UNIVERSAL ===")
print("Funciona con cualquier versión de Flet")

import flet as ft
import random
from datetime import datetime

def main(page):
    # Configuración básica
    page.title = "💰 Control Financiero"
    page.window_width = 800
    page.window_height = 700
    page.padding = 20
    
    # Variables de estado
    saldo = 0.0
    ingresos = 0.0
    gastos = 0.0
    transacciones = []
    
    # ========== INTERFAZ SIMPLIFICADA ==========
    
    # Título
    titulo = ft.Text("💰 GESTOR FINANCIERO", 
                    size=28, 
                    weight="bold",
                    text_align="center")
    
    # Panel de estadísticas
    panel_estadisticas = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text("SALDO", size=14),
                ft.Text("$0.00", size=30, weight="bold")
            ], horizontal_alignment="center"),
            padding=15,
            border=ft.border.all(2),
            border_radius=10,
            width=170
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("INGRESOS", size=14),
                ft.Text("$0.00", size=24, color="green")
            ], horizontal_alignment="center"),
            padding=15,
            border=ft.border.all(1),
            border_radius=10,
            width=150
        ),
        ft.Container(
            content=ft.Column([
                ft.Text("GASTOS", size=14),
                ft.Text("$0.00", size=24, color="red")
            ], horizontal_alignment="center"),
            padding=15,
            border=ft.border.all(1),
            border_radius=10,
            width=150
        )
    ], alignment="center", spacing=20)
    
    # Formulario
    campo_monto = ft.TextField(
        label="Monto ($)",
        width=200,
        hint_text="Ej: 1500.50",
        prefix_text="$"
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
            ft.dropdown.Option("Salario"),
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
    
    campo_desc = ft.TextField(
        label="Descripción",
        width=400,
        hint_text="Detalles de la transacción..."
    )
    
    # Lista de transacciones
    lista_transacciones = ft.Column(
        spacing=8,
        scroll="auto",
        height=250
    )
    
    # ========== FUNCIONES ==========
    def actualizar_panel():
        # Actualizar valores en el panel
        panel_estadisticas.controls[0].content.controls[1].value = f"${saldo:,.2f}"
        panel_estadisticas.controls[1].content.controls[1].value = f"${ingresos:,.2f}"
        panel_estadisticas.controls[2].content.controls[1].value = f"${gastos:,.2f}"
        
        # Color del saldo
        if saldo >= 0:
            panel_estadisticas.controls[0].content.controls[1].color = "green"
        else:
            panel_estadisticas.controls[0].content.controls[1].color = "red"
    
    def agregar_transaccion(e):
        nonlocal saldo, ingresos, gastos
        
        if not campo_monto.value:
            campo_monto.error_text = "Ingrese un monto"
            page.update()
            return
        
        try:
            monto = float(campo_monto.value)
            tipo = radio_tipo.value
            categoria = dropdown_categoria.value
            descripcion = campo_desc.value
            fecha = datetime.now().strftime("%d/%m %H:%M")
            trans_id = random.randint(1000, 9999)
            
            # Actualizar valores
            if tipo == "ingreso":
                saldo += monto
                ingresos += monto
                color_texto = "green"
                simbolo = "▲"
            else:
                saldo -= monto
                gastos += monto
                color_texto = "red"
                simbolo = "▼"
            
            # Agregar registro
            transacciones.append({
                "id": trans_id,
                "monto": monto,
                "tipo": tipo,
                "categoria": categoria,
                "fecha": fecha
            })
            
            # Agregar a la lista visual
            item_texto = f"{simbolo} ${monto:,.2f} | {categoria} | {fecha} | #{trans_id}"
            lista_transacciones.controls.insert(
                0, 
                ft.Text(item_texto, color=color_texto)
            )
            
            # Actualizar panel
            actualizar_panel()
            
            # Limpiar campos
            campo_monto.value = ""
            campo_desc.value = ""
            campo_monto.error_text = None
            
            page.update()
            
            print(f"Transacción #{trans_id} agregada")
            
        except ValueError:
            campo_monto.error_text = "Número inválido"
            page.update()
    
    def limpiar_todo(e):
        nonlocal saldo, ingresos, gastos
        saldo = 0.0
        ingresos = 0.0
        gastos = 0.0
        transacciones.clear()
        lista_transacciones.controls.clear()
        actualizar_panel()
        page.update()
        print("Todo limpiado")
    
    # Botones
    boton_agregar = ft.ElevatedButton(
        "Agregar Transacción",
        on_click=agregar_transaccion,
        width=200
    )
    
    boton_limpiar = ft.OutlinedButton(
        "Limpiar Todo",
        on_click=limpiar_todo,
        width=150
    )
    
    # ========== CONSTRUIR INTERFAZ ==========
    page.add(
        ft.Column([
            titulo,
            ft.Divider(height=20),
            
            panel_estadisticas,
            
            ft.Divider(height=30),
            
            ft.Text("📝 Nueva Transacción", size=20),
            
            ft.Row([
                campo_monto,
                dropdown_categoria
            ]),
            
            ft.Container(height=10),
            
            ft.Row([
                ft.Text("Tipo:", size=16),
                radio_tipo
            ]),
            
            ft.Container(height=10),
            
            campo_desc,
            
            ft.Container(height=15),
            
            ft.Row([
                boton_agregar,
                boton_limpiar
            ], alignment="center"),
            
            ft.Divider(height=30),
            
            ft.Text("📋 Historial", size=20),
            
            ft.Container(
                content=lista_transacciones,
                border=ft.border.all(1),
                padding=15,
                border_radius=10,
                height=270
            ),
            
            ft.Text(f"Total: {len(transacciones)} transacciones", 
                   size=12, color="gray")
        ], scroll="auto", spacing=15)
    )
    
    print("✅ Aplicación lista en http://localhost:8888")

# Iniciar
if __name__ == "__main__":
    ft.app(target=main, port=8888)
