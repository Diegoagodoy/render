from fastapi import FastAPI

from models import RenderRequest
from service import RenderService


app = FastAPI(
    title="HTML Render Service",
    version="1.0.0",
    description="Microservicio para convertir HTML en imágenes PNG mediante Playwright."
)


@app.get("/")
def home():

    return {
        "status": "OK",
        "service": "HTML Render Service",
        "version": "1.0.0"
    }


@app.get("/health")
def health():

    return {
        "status": "UP",
        "playwright": "OK"
    }


@app.post("/render")
def render(request: RenderRequest):

    service = RenderService()

    return service.process(request)