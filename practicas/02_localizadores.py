"""Práctica 2: utiliza localizadores semánticos."""

from playwright.sync_api import sync_playwright

PORTAL = "http://127.0.0.1:8000"

with sync_playwright() as playwright:
    # En esta práctica el navegador se deja visible para observar la página.
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(PORTAL)

    # TODO 1: localizar el encabezado principal por su rol.
    # get_by_role() utiliza la semántica accesible del documento. Para un
    # encabezado se indica el rol "heading" y su nombre visible.
    encabezado = page.get_by_role(
        "heading",
        name="Consulta de kárdex",
    )

    # TODO 2: localizar el campo por su etiqueta "Matrícula".
    # get_by_label() relaciona un control con la etiqueta que ve el usuario.
    # Es más expresivo que depender de coordenadas o clases de diseño.
    campo = page.get_by_label("Matrícula")

    # TODO 3: localizar el botón por su rol y nombre.
    # Un buen localizador comunica qué elemento se necesita y para qué sirve.
    boton = page.get_by_role("button", name="Buscar")

    # TODO 4: imprimir el texto del encabezado y verificar visibilidad.
    # text_content() recupera contenido; is_visible() consulta el estado visual.
    # Crear un Locator no ejecuta todavía una acción sobre la página.
    print("Encabezado:", encabezado.text_content())
    print("Campo visible:", campo.is_visible())
    print("Botón visible:", boton.is_visible())

    # Los localizadores se vuelven a resolver cuando se usan, lo que ayuda a
    # trabajar con páginas que cambian dinámicamente.
    browser.close()