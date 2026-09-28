"""Práctica 3: conserva evidencia de la ejecución."""

from pathlib import Path
from playwright.sync_api import sync_playwright

# __file__ es la ubicación de este script. parents[1] permite obtener la raíz
# del laboratorio independientemente del directorio desde el que se ejecute.
ROOT = Path(__file__).resolve().parents[1]
PORTAL = "http://127.0.0.1:8000"
EVIDENCIAS = ROOT / "evidencias"

# exist_ok=True evita un error cuando la carpeta ya existe.
EVIDENCIAS.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 1: guardar una captura completa como portal.png.
    # page.screenshot(..., full_page=True) incluye el contenido que podría
    # encontrarse fuera del área visible de la ventana.
    page.screenshot(
        path=EVIDENCIAS / "portal.png",
        full_page=True,
    )

    # TODO 2: localizar el encabezado y guardar encabezado.png.
    # Un Locator también ofrece screenshot(); así se captura únicamente el
    # elemento relevante y no toda la página.
    page.get_by_role(
        "heading",
        name="Consulta de kárdex",
    ).screenshot(
        path=EVIDENCIAS / "encabezado.png"
    )

    # Las capturas apoyan la trazabilidad, pero no sustituyen la validación del
    # resultado ni los logs. Deben generarse con una finalidad clara.
    browser.close()

print("Revise la carpeta:", EVIDENCIAS)