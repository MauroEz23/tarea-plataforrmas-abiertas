# API Estudiantes - Prácticas 2 y 3

Este proyecto es una API RESTful básica desarrollada en Python utilizando el microframework Flask. Fue creada para el curso de **Desarrollo con Plataformas Abiertas** e incluye los endpoints de la Práctica 2 y los métodos HTTP (CRUD simulado) de la Práctica 3.

## 🛠️ Tecnologías utilizadas
*   **Python** (Lenguaje de programación)
*   **Flask** (Framework web para crear los endpoints)
*   **Flask-CORS** (Para permitir peticiones desde cualquier origen)

## 📁 Estructura del proyecto
El proyecto está organizado de forma modular para separar la configuración, el arranque y la lógica de las rutas:

```text
tarea-plataforrmas-abiertas/
│   README.md
│   .gitignore
│   requirements.txt
├───data/                  # Carpeta reservada para futuras bases de datos
└───v1/
    ├───run.py             # Archivo principal que arranca la API
    └───app/
        ├───__init__.py    # Crea y configura la aplicación Flask
        └───controllers/
            └───estudiantes.py  # Lógica de los endpoints de la API