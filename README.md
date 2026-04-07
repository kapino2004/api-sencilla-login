# API Sencilla de Login con FastAPI y SQLModel

Esta es una API REST mínima construida con FastAPI que implementa un proceso de login básico contra una base de datos local usando `sqlmodel`. 

La base de datos se inicializa automáticamente al arrancar la aplicación y contiene un usuario por defecto. **No implementa JWT ni manejo de sesiones complejas**, su propósito es puramente educativo para entender el flujo de validación.

## Requisitos previos
* Python 3.10 o superior.

## Instalación y ejecución

1. **Clone este repositorio** y navegue a la carpeta del proyecto.
2. **Cree un entorno virtual**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate

Instale las dependencias:

Bash
pip install -r requirements.txt
Ejecuta el servidor:

Bash
uvicorn main:app --reload
La API estará disponible en http://127.0.0.1:8000.

Usuario por defecto (Credenciales)
Al iniciar la aplicación, se crea automáticamente el siguiente usuario para pruebas:

Username: admin

Password: password123
