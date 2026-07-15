from typing import List, Optional

from pydantic import BaseModel


# =========================
# REQUEST
# =========================

class Trabajo(BaseModel):

    region: str
    sitio: str
    html: str


class RenderRequest(BaseModel):

    callback: bool = False
    callback_url: Optional[str] = None

    tipo_reporte: str
    fecha_reporte: str

    trabajos: List[Trabajo]



# =========================
# RESPONSE
# =========================

class Imagen(BaseModel):

    sitio: str
    estado: str
    mensaje: Optional[str] = None
    imagen: Optional[str] = None



class Region(BaseModel):

    region: str
    imagenes: List[Imagen]



class RenderResponse(BaseModel):

    status: str

    tipo_reporte: str
    fecha_reporte: str

    regiones: List[Region]