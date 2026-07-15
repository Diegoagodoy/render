import requests
import urllib3 #solo para prueba

urllib3.disable_warnings()

class CallbackService:


    def __init__(self):

        self.timeout = 120


    def send(
        self,
        url: str,
        payload: dict
    ):

        response = requests.post(
            url,
            json=payload,
            timeout=self.timeout,
            verify=False # Solo para Prueba!!! hay que chequearlo
        )

        response.raise_for_status()

        return {
            "status_code": response.status_code,
            "response": response.text
        }