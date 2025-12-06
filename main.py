#!/usr/bin/env python3
"""
Sistema de Control Financiero Personal
Aplicación principal para gestionar ingresos y gastos.
"""

print("=== INICIANDO SISTEMA FINANZAS ===")
print("Cargando...")

import flet as ft
from control.logic import Controller

def main(page: ft.Page):
    """Función principal que inicia la aplicación."""
    # Crear el controlador que maneja todo
    controller = Controller(page)

    print("✅ Aplicación lista!")
    print("🌐 Abre: http://localhost:8888")

# Punto de entrada
if __name__ == "__main__":
    print("🚀 Iniciando aplicación de finanzas...")
    ft.app(target=main, port=8888)
