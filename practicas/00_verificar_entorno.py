"""Práctica 0: verifica que Playwright y Chromium estén disponibles."""

from playwright.sync_api import sync_playwright

# Dirección del portal local. El servidor debe estar ejecutándose en otra
# terminal antes de iniciar esta práctica.
PORTAL = "http://127.0.0.1:8000"

# sync_playwright() inicia la API síncrona de Playwright. El bloque with se
# encarga de liberar sus recursos al terminar, incluso si ocurre un error.
with sync_playwright() as playwright:
    # chromium representa el tipo de navegador. launch() crea una instancia
    # nueva; no es necesario abrir Chrome o Chromium manualmente.
    # headless=False permite observar la ventana durante el aprendizaje.
    browser = playwright.chromium.launch(headless=False)

    # Una Page representa una pestaña del navegador. Desde este objeto se
    # realizan la navegación, localización e interacción con la interfaz.
    page = browser.new_page()

    # goto() navega a una URL y espera a que la página alcance el estado de
    # carga correspondiente. Si el servidor no está activo, esta línea falla.
    page.goto(PORTAL)

    # title() consulta el título del documento. url es una propiedad con la
    # dirección actual. Ambos valores constituyen evidencia básica.
    print("Título:", page.title())
    print("URL:", page.url)

    # Esta pausa solo permite observar la ventana durante la demostración.
    # No debe usarse como estrategia general para sincronizar un bot.
    page.wait_for_timeout(1500)

    # Cerrar explícitamente el navegador evita dejar procesos activos.
    browser.close()

print("Entorno listo.")
