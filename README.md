# Flask Projecto

Este es un proyecto básico de Flask que utiliza SQLAlchemy para manejar la base de datos SQLite. A continuación se detallan los pasos para configurar y ejecutar el proyecto.

## Requisitos

- Python 3.x
- pip (el gestor de paquetes de Python)
- Virtualenv (opcional pero recomendado)

## Instrucciones de Instalación


1. **Crear un Entorno Virtual (necesario)**: Es recomendable usar un entorno virtual para evitar conflictos con otras instalaciones de Python. Para crear un entorno virtual, ejecuta:

    ```bash
    python -m venv env
    ```

2. **Activar el Entorno Virtual**:
    - En Windows:

        ```bash
        env\Scripts\activate
        ```

    - En MacOS/Linux:

        ```bash
        source env/bin/activate
        ```

4. **Instalar las Dependencias**: Instala las dependencias del proyecto que se encuentran en el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Configuración de la Base de Datos**: Este proyecto utiliza SQLite como base de datos. Para crear la base de datos, sigue estos pasos:

    - Asegúrate de estar en el entorno virtual (si lo estás utilizando).
    - Abre una sesión interactiva de Python en la terminal:

        ```bash
        python
        ```
        o bien ejecutando el shell interactivo con 

      ```bash
        ipython
        ```
    - Dentro de la sesión de Python, ejecuta los siguientes comandos para crear la base de datos:

        ```python
        from app import app, db
        with app.app_context():
            db.create_all()
        ```

    Esto creará un archivo de base de datos SQLite en el directorio del proyecto.

6. **Ejecutar la Aplicación**: Para iniciar la aplicación Flask, ejecuta el siguiente comando:

    ```bash
    python app.py
    ```

    La aplicación estará disponible en `http://127.0.0.1:5000/` en tu navegador.

## Estructura del Proyecto

La estructura básica del proyecto es la siguiente:

flask_projecto/
├── app.py          # Archivo principal de la aplicación Flask
├── models.py       # Definición de modelos SQLAlchemy
├── templates/      # Plantillas HTML
│   ├── base.html
│   ├── inicio.html
│   └── agregar.html
├── static/# Archivos estáticos (CSS, JavaScript, imágenes)
|   ├── style.css
├── env/            # Entorno virtual 
└── README.md       # Este archivo


