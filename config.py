import os


class Settings:

    # Aplicación
    APP_NAME = "HTML Render Service"
    VERSION = "1.0.0"


    # Render
    HTML_SELECTOR = os.getenv(
        "HTML_SELECTOR",
        "#report-container"
    )

    PLAYWRIGHT_TIMEOUT = int(
        os.getenv(
            "PLAYWRIGHT_TIMEOUT",
            "30000"
        )
    )


    # Callback
    CALLBACK_TIMEOUT = int(
        os.getenv(
            "CALLBACK_TIMEOUT",
            "120"
        )
    )

    CALLBACK_RETRIES = int(
        os.getenv(
            "CALLBACK_RETRIES",
            "3"
        )
    )



    # Ambiente
    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "DEV"
    )


settings = Settings()