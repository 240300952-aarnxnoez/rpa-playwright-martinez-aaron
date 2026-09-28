"""Práctica 4: completa el formulario y clasifica el resultado."""

from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8000"

# La matrícula es un parámetro de entrada. Declararla una sola vez facilita
# cambiar el caso de prueba sin modificar varias instrucciones.
MATRICULA = "IAI0001"

with sync_playwright() as playwright:
    # slow_mo facilita observar cada interacción durante la práctica.
    browser = playwright.chromium.launch(headless=False, slow_mo=250)
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 1: llenar el campo Matrícula con MATRICULA.
    # fill() reemplaza el contenido del campo; no simula tecla por tecla.
    page.get_by_label("Matrícula").fill(MATRICULA)

    # TODO 2: presionar el botón Buscar.
    # click() incorpora verificaciones previas: el elemento debe existir,
    # estar visible, estable y en condiciones de recibir la acción.
    page.get_by_role("button", name="Buscar").click()

    # TODO 3: localizar el panel mediante data-testid="result-panel".
    # get_by_test_id() resulta útil cuando la interfaz incluye un identificador
    # estable creado deliberadamente para automatización o pruebas.
    panel = page.get_by_test_id("result-panel")

    # TODO 4: imprimir el texto del panel.
    # inner_text() devuelve el texto visible consolidado. Este valor puede
    # convertirse en una regla para clasificar el resultado.
    texto = panel.inner_text()
    print(texto)

    # TODO 5: repetir con IAI9999 e identificar la excepción de negocio.
    # Una matrícula inexistente es una excepción de negocio: la aplicación y
    # el bot funcionan, pero los datos no satisfacen una regla del proceso.
    page.get_by_label("Matrícula").fill("IAI9999")
    page.get_by_role("button", name="Buscar").click()

    texto = panel.inner_text()
    print(texto)

    if "Matrícula inexistente" in texto:
        print("EXCEPCIÓN DE NEGOCIO")

    browser.close()