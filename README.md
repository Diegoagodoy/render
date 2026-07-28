
# HTML Render Service

Microservicio FastAPI para convertir HTML en imágenes PNG utilizando Playwright Chromium.

## Instalación

Crear entorno:

python -m venv venv

Activar:

Windows:

venv\Scripts\activate

Linux:

source venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Instalar navegador Playwright:

playwright install chromium

## Ejecutar

uvicorn app:app --reload

## Endpoints

GET /

GET /docs

GET /health

POST /render
