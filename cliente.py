import requests

URL = "http://localhost:8000/render"

html = """
<html>

<body>

<div id="report-container"
     style="
        width:800px;
        padding:30px;
        background:#f3f5f9;
        font-family:Arial;
     ">

<h1>Hola desde el Cliente</h1>

<p>Este HTML simula el generado por Airflow.</p>

</div>

</body>

</html>
"""

payload = {
    "callback_url": "",
    "tipo_reporte": "DIARIO",
    "fecha_reporte": "2026-07-15",
    "trabajos": [
        {
            "region": "AMBA",
            "sitio": "QUI",
            "html": html
        }
    ]
}

response = requests.post(
    URL,
    json=payload,
    timeout=120
)

print(response.status_code)

respuesta = response.json()

print(respuesta["status"])

print(
    respuesta["regiones"][0]["imagenes"][0]["sitio"]
)

print(
    respuesta["regiones"][0]["imagenes"][0]["imagen"][:100]
)