print("=== SISTEMA FINANZAS SIMPLIFICADO ===")

import flet as ft
import random
from datetime import datetime

def main(page):
    page.title = "Finanzas Mejorado"
    page.window_width = 900
    page.window_height = 750
    
    # Variables
    saldo = 0
    ingresos = 0
    gastos = 0
    transacciones = []
    
    # ========== COMPONENTES ==========
    
    # Tarjetas de resumen
    tarjeta_saldo = ft.Container(
        content=ft.Column([
            ft.Text("SALDO", size=14),
            ft.Text("$0", size=30, weight="bold")
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15,
        border=ft.border.all(2),
        border_radius=10,
        width=160
    )
    
    tarjeta_ingresos = ft.Container(
        content=ft.Column([
            ft.Text("INGRESOS", size=14),
            ft.Text("$0", size=24)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15,
        border=ft.border.all(1),
        border_radius=10,
        width=140
    )
    
    tarjeta_gastos = ft.Container(
        content=ft.Column([
            ft.Text("GASTOS", size=14),
            ft.Text("$0", size=24)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=15,
        border=ft.border.all(1),
        border_radius=10,
        width=140
    )
    
    # Formulario
    campo_monto = ft.TextField(label="Monto ($)", width=200)
    campo_categoria = ft.TextField(label="Categoría", width=200, value="General")
    campo_descripcion = ft.TextField(label="Descripción", width=400, multiline=True)
    
    # Lista de transacciones
    lista = ft.Column(scroll=True, height=300)
    
    def actualizar_resumen():
        tarjeta_saldo.content.controls[1].value = f"${saldo}"
        tarjeta_ingresos.content.controls[1].value = f"${ingresos}"
        tarjeta_gastos.content.controls[1].value = f"${gastos}"
    
    def agregar_ingreso(e):
        nonlocal saldo, ingresos
        if campo_monto.value:
            try:
                monto = float(campo_monto.value)
                saldo += monto
                ingresos += monto
                
                # Agregar a lista
                hora = datetime.now().strftime("%H:%M")
                lista.controls.insert(0, ft.Text(f"[{hora}] +${monto} - {campo_categoria.value}"))
                
                # Actualizar
                actualizar_resumen()
                campo_monto.value = ""
                campo_descripcion.value = ""
                page.update()
                
            except:
                campo_monto.error_text = "Error"
                page.update()
    
    def agregar_gasto(e):
        nonlocal saldo, gastos
        if campo_monto.value:
            try:
                monto = float(campo_monto.value)
                saldo -= monto
                gastos += monto
                
                # Agregar a lista
                hora = datetime.now().strftime("%H:%M")
                lista.controls.insert(0, ft.Text(f"[{hora}] -${monto} - {campo_categoria.value}", color="red"))
                
                # Actualizar
                actualizar_resumen()
                campo_monto.value = ""
                campo_descripcion.value = ""
                page.update()
                
            except:
                campo_monto.error_text = "Error"
                page.update()
    
    def limpiar_todo(e):
        nonlocal saldo, ingresos, gastos
        saldo = 0
        ingresos = 0
        gastos = 0
        lista.controls.clear()
        actualizar_resumen()
        page.update()
    
    # Layout
    page.add(
        ft.Column([
            ft.Text("💰 CONTROL FINANCIERO COMPLETO", size=26, weight="bold", text_align="center"),
            
            ft.Row([tarjeta_saldo, tarjeta_ingresos, tarjeta_gastos], alignment="center"),
            
            ft.Divider(height=30),
            
            ft.Text("📝 Nueva Transacción", size=20),
            
            ft.Row([campo_monto, campo_categoria]),
            
            campo_descripcion,
            
            ft.Row([
                ft.ElevatedButton("➕ Agregar Ingreso", on_click=agregar_ingreso, width=180),
                ft.ElevatedButton("➖ Agregar Gasto", on_click=agregar_gasto, width=180, color="red"),
                ft.OutlinedButton("🗑️ Limpiar Todo", on_click=limpiar_todo, width=180)
            ], alignment="center"),
            
            ft.Divider(height=30),
            
            ft.Text("📋 Historial", size=20),
            
            ft.Container(
                content=lista,
                border=ft.border.all(2),
                padding=15,
                border_radius=10,
                height=320
            ),
            
            ft.Text(f"Total transacciones: {len(transacciones)}", size=12, color="grey")
        ], scroll=True, spacing=15)
    )

ft.app(target=main, port=8888)
