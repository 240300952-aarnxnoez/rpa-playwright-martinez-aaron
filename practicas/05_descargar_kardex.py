"""Práctica 5: espera y guarda una descarga."""

from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PORTAL = "http://127.0.0.1:8000"
MATRICULA = "IAI0002"
DESCARGAS = ROOT / "descargas"
DESCARGAS.mkdir(exist_ok=True)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=250)
    page = browser.new_page()
    page.goto(PORTAL)

    page.get_by_label("Matrícula").fill(MATRICULA)
    page.get_by_role("button", name="Buscar").click()

    # TODO 1: utilizar page.expect_download() alrededor del clic.
    # La espera debe declararse ANTES de hacer clic, porque el evento de
    # descarga puede comenzar inmediatamente. La estructura esperada es:
    # with page.expect_download() as download_info:
    #     ...hacer clic en Descargar kárdex...
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Descargar kárdex").click()

    # TODO 2: obtener download_info.value.
    # value proporciona el objeto Download cuando el evento ya fue capturado.
    download = download_info.value

    # TODO 3: guardar como descargas/kardex-<MATRICULA>.pdf.
    # download.save_as(...) permite controlar la carpeta y el nombre final;
    # no se debe depender de la carpeta predeterminada del navegador.
    destino = DESCARGAS / f"kardex-{MATRICULA}.pdf"
    download.save_as(destino)

    # TODO 4: imprimir la ruta final.
    # Informar el resultado mejora la trazabilidad y permite verificarlo.
    print("Descarga guardada en:", destino)

    browser.close()