"""Práctica 1: abre el portal y recupera información de la página."""

from playwright.sync_api import sync_playwright

# Centralizar la URL evita repetir valores de configuración en el flujo.
PORTAL = "http://127.0.0.1:8000"

# El administrador de contexto inicia y detiene Playwright automáticamente.
with sync_playwright() as playwright:
    # TODO 1: iniciar Chromium en modo visible y con slow_mo=300.
    # headless=False muestra la ventana; slow_mo hace perceptibles las acciones.
    # Ninguno de estos parámetros sustituye las esperas automáticas.
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300,
    )

    # TODO 2: crear una página y navegar a PORTAL.
    # browser.new_page() devuelve una pestaña controlable mediante Page.
    # page.goto(...) establece el estado inicial de la automatización.
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 3: imprimir el título y la URL.
    # El título se obtiene con un método; la URL se consulta como propiedad.
    print("Título:", page.title())
    print("URL:", page.url)

    # TODO 4: cerrar el navegador.
    # La liberación de recursos forma parte de una ejecución controlada.
    browser.close()