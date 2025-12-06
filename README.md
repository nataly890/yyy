<<<<<<< HEAD
# Sistema de Control Financiero Personal

Una aplicación de escritorio para gestionar ingresos y gastos personales, construida con Python y Flet.

## Características

- ✅ Gestión de ingresos y gastos
- ✅ Seguimiento de saldo en tiempo real
- ✅ Historial de transacciones
- ✅ Interfaz gráfica intuitiva
- ✅ Base de datos SQLite integrada
- ✅ Arquitectura MVC (Modelo-Vista-Controlador)

## Estructura del Proyecto

```
finanzas/
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── modelo/                # Capa de datos
│   ├── __init__.py
│   ├── database.py        # Gestión de base de datos SQLite
│   └── finanzas.db        # Archivo de base de datos
├── vista/                 # Capa de presentación
│   ├── __init__.py
│   └── ui.py              # Componentes de interfaz de usuario
└── control/               # Capa de lógica de negocio
    ├── __init__.py
    └── logic.py           # Controlador principal
```

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga el proyecto:**
   ```bash
   git clone <url-del-repositorio>
   cd finanzas
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python main.py
   ```

4. **Accede a la aplicación:**
   - Abre tu navegador web en: `http://localhost:8888`
   - La aplicación se abrirá automáticamente en una ventana dedicada

## Uso

### Agregar Transacciones

1. Ingresa el monto en el campo "Monto ($)"
2. Selecciona el tipo: "Ingreso" o "Gasto"
3. Haz clic en "Agregar Transacción"
4. El saldo se actualizará automáticamente
5. La transacción aparecerá en el historial

### Limpiar Datos

- Haz clic en "Limpiar Todo" para resetear el saldo y eliminar todas las transacciones

## Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación principal
- **Flet**: Framework para aplicaciones web/desktop con Flutter
- **SQLite**: Base de datos embebida para almacenamiento local

## Arquitectura MVC

- **Modelo (modelo/)**: Maneja la lógica de datos y persistencia
- **Vista (vista/)**: Gestiona la interfaz de usuario y presentación
- **Controlador (control/)**: Coordina la interacción entre modelo y vista

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio.

---

¡Gracias por usar el Sistema de Control Financiero Personal!
=======
# yyy
>>>>>>> fed0fc672ac2bf11a85d0bda775822e4b3e77de5
