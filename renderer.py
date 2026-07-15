import base64

from playwright.sync_api import sync_playwright


class Renderer:

    def __init__(self):

        print("Inicializando Chromium...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-software-rasterizer"
            ]
        )

        print("Chromium iniciado OK")


    def render(self, html: str) -> str:

        page = self.browser.new_page()

        try:
            page.set_content(html)

            page.wait_for_load_state("networkidle")

            page.wait_for_timeout(500)

            element = page.locator("#report-container")

            png = element.screenshot()

            return base64.b64encode(png).decode("utf-8")

        finally:
            page.close()


    def close(self):

        self.browser.close()
        self.playwright.stop()