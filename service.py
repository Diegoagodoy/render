from collections import defaultdict
from callback import CallbackService

from models import (
    RenderRequest,
    RenderResponse,
    Region,
    Imagen
)

from renderer import Renderer


class RenderService:

    def __init__(self):

        self.renderer = Renderer()


    def process(
        self,
        request: RenderRequest
    ) -> RenderResponse:

        regiones = defaultdict(list)

        try:

            for trabajo in request.trabajos:

                print(
                    f"Renderizando {trabajo.sitio}"
                )

                try:

                    imagen = self.renderer.render(
                        trabajo.html
                    )

                    regiones[trabajo.region].append(
                        Imagen(
                            sitio=trabajo.sitio,
                            estado="OK",
                            mensaje=None,
                            imagen=imagen
                        )
                    )


                except Exception as e:

                    print(
                        f"Error {trabajo.sitio}: {e}"
                    )

                    regiones[trabajo.region].append(
                        Imagen(
                            sitio=trabajo.sitio,
                            estado="ERROR",
                            mensaje=str(e),
                            imagen=None
                        )
                    )


            respuesta = RenderResponse(
                status="OK",
                tipo_reporte=request.tipo_reporte,
                fecha_reporte=request.fecha_reporte,
                regiones=[
                    Region(
                        region=region,
                        imagenes=imagenes
                    )
                    for region, imagenes in regiones.items()
                ]
            )


            if request.callback and request.callback_url:

                callback = CallbackService()

                callback.send(
                    request.callback_url,
                    respuesta.model_dump()
                )

                return {
                    "status": "ENVIADO",
                    "imagenes": sum(
                        len(r.imagenes)
                        for r in respuesta.regiones
                    )
                }


            return respuesta


        finally:

            self.renderer.close()