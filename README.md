# Laboratorio: primeros pasos con Playwright y Python

Proyecto introductorio para explorar automatización web con Playwright desde Visual Studio Code. El laboratorio utiliza un portal escolar local y datos completamente sintéticos.

## ¿Qué es Playwright?

[Playwright](https://playwright.dev/python/) es una librería de automatización de navegadores desarrollada por Microsoft. Permite controlar mediante código aplicaciones web ejecutadas en Chromium, Firefox y WebKit. Aunque surgió principalmente para pruebas de software, su API también puede emplearse para automatizar tareas web de propósito general.

En este laboratorio se utilizará Playwright para reproducir acciones que normalmente realizaría una persona:

- abrir un navegador;
- visitar una dirección web;
- localizar campos y botones;
- introducir una matrícula;
- leer el resultado presentado por el sistema;
- iniciar y guardar una descarga;
- capturar evidencia de la ejecución.

Playwright resulta especialmente útil para introducir RPA web porque trabaja con la estructura de la página y no con coordenadas de pantalla. En lugar de indicar «haz clic en la posición 520, 340», se expresa la intención de la interacción:

```python
page.get_by_label("Matrícula").fill("IAI0001")
page.get_by_role("button", name="Buscar").click()
```

Este enfoque tiende a ser más legible y resistente ante cambios de resolución o pequeñas modificaciones visuales.

### Modelo de objetos utilizado

```text
Playwright
└── BrowserType: chromium
    └── Browser
        └── BrowserContext
            └── Page
                └── Locator
```

| Elemento | Responsabilidad |
|---|---|
| `sync_playwright()` | Inicia y finaliza el acceso a Playwright mediante su API síncrona. |
| `playwright.chromium` | Representa el tipo de navegador Chromium. |
| `Browser` | Es la instancia del navegador controlada por el bot. |
| `BrowserContext` | Representa una sesión aislada, con sus propias cookies y almacenamiento. En estas prácticas se crea implícitamente. |
| `Page` | Representa una pestaña del navegador; permite navegar, localizar e interactuar. |
| `Locator` | Describe cómo encontrar uno o varios elementos de la interfaz. |

Se utiliza la API síncrona porque permite leer las instrucciones en el mismo orden en que se ejecutan. Más adelante puede compararse con la API asíncrona para procesos concurrentes.

### Navegador visible y headless

```python
browser = playwright.chromium.launch(headless=False, slow_mo=300)
```

- `headless=False` muestra la ventana y facilita observar las acciones durante el aprendizaje.
- `headless=True` ejecuta el navegador sin interfaz visible y suele utilizarse en servidores o ejecuciones desatendidas.
- `slow_mo=300` agrega 300 milisegundos entre operaciones para que el movimiento sea perceptible. No debe utilizarse como mecanismo de sincronización.

Playwright incorpora esperas automáticas antes de las interacciones. Por ejemplo, antes de pulsar un botón espera que el elemento exista y pueda recibir la acción. Por ello, no se recomienda agregar pausas arbitrarias para «dar tiempo» a la página.

## Resultado de aprendizaje

Al terminar, el estudiante construye un bot que:

1. abre un navegador;
2. consulta una matrícula;
3. identifica un resultado de éxito o error;
4. descarga un kárdex sintético;
5. conserva una captura y un registro básico de la ejecución.

## Duración

La ruta esencial está diseñada para 30-40 minutos de trabajo guiado. Las extensiones permiten continuar en una segunda sesión.

## Estructura

```text
playwright_kardex/
├── .vscode/                 Configuración y tareas de VS Code
├── app/                     Portal escolar local
├── evidencias/              Capturas generadas por los bots
├── descargas/               Kárdex descargados
├── practicas/               Archivos que completa el estudiante
├── soluciones_docente/      Implementaciones de referencia
├── server.py                Servidor local sin dependencias externas
├── requirements.txt
└── README.md
```

## Preparación antes de la clase

### 1. Abrir el proyecto

En VS Code, seleccione **Archivo > Abrir carpeta** y abra `playwright_kardex`.

### 2. Crear el entorno virtual

macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar Playwright

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 4. Seleccionar el intérprete

Abra la paleta de comandos de VS Code y ejecute:

```text
Python: Select Interpreter
```

Seleccione el intérprete ubicado en `.venv`.

### 5. Verificar el entorno

```bash
python practicas/00_verificar_entorno.py
```

Debe abrirse Chromium, mostrarse el portal y cerrarse automáticamente.

## Ejecución durante el laboratorio

### Terminal 1: iniciar el portal

```bash
python server.py
```

También puede usar la tarea de VS Code **RPA: iniciar portal local**.

Abra <http://127.0.0.1:8000> para comprobar que el portal funciona.

### Terminal 2: ejecutar prácticas

```bash
python practicas/01_navegar.py
python practicas/02_localizadores.py
python practicas/03_evidencia.py
python practicas/04_consultar_estudiante.py
python practicas/05_descargar_kardex.py
python practicas/06_reto_integrador.py
```

## Cómo trabajar el laboratorio

El laboratorio se desarrolla en orden. No comience una práctica hasta que la anterior produzca el resultado esperado.

1. Mantenga `server.py` ejecutándose en la **Terminal 1** durante toda la sesión.
2. Utilice la **Terminal 2** para ejecutar los archivos de `practicas/`.
3. Abra cada archivo en VS Code y lea primero su encabezado y comentarios.
4. Localice las instrucciones marcadas con `TODO`.
5. Complete un `TODO` a la vez y ejecute nuevamente el archivo.
6. Observe la ventana de Chromium y la salida de la terminal.
7. Corrija el código hasta obtener el resultado esperado.
8. Guarde el archivo antes de continuar con la siguiente práctica.

La práctica 0 es únicamente una **comprobación técnica**. El código está completo y no debe copiarse ni modificarse. Las prácticas 1 a 5 son ejercicios guiados; la práctica 6 es el reto integrador.

### Convenciones de los archivos

- `TODO`: instrucción que debe completar el estudiante.
- `PORTAL`: dirección de la aplicación local.
- `MATRICULA`: entrada del caso de prueba.
- `ROOT`: ruta raíz del proyecto.
- `EVIDENCIAS`: carpeta para capturas.
- `DESCARGAS`: carpeta para los kárdex generados.

No consulte `soluciones_docente/` durante el desarrollo. El objetivo no es solamente lograr que el bot funcione, sino comprender cada instrucción utilizada.

### Si una práctica falla

1. Lea desde la última línea del mensaje de error.
2. Compruebe que `server.py` siga activo.
3. Verifique que la URL sea `http://127.0.0.1:8000`.
4. Confirme que VS Code utiliza el intérprete de `.venv`.
5. Revise el último `TODO` modificado.
6. Compare el nombre visible del elemento con el localizador utilizado.

No agregue `time.sleep()` para ocultar errores de sincronización. Playwright ya espera automáticamente que los elementos estén disponibles para la mayoría de las acciones.

## Datos sintéticos

| Matrícula | Resultado |
|---|---|
| `IAI0001` | Ada Lovelace |
| `IAI0002` | Alan Turing |
| `IAI0003` | Grace Hopper |
| `IAI9999` | Matrícula inexistente |

## Ruta de prácticas

### Práctica 0. Comprobación técnica del entorno

Esta actividad no es un ejercicio de programación. Su propósito es comprobar que Python, Playwright, Chromium y el portal local están disponibles antes de comenzar.

Archivo: `practicas/00_verificar_entorno.py`.

El bloque:

```python
with sync_playwright() as playwright:
```

inicia Playwright y garantiza que sus recursos se liberen al terminar. La variable `playwright` proporciona acceso a los navegadores compatibles.

```python
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
```

La primera instrucción crea una instancia de Chromium y la segunda abre una pestaña. La ventana no necesita estar abierta antes de ejecutar el programa: Playwright la inicia automáticamente.

```python
page.goto(PORTAL)
```

Navega al servidor local. Para que funcione, `server.py` debe permanecer activo en otra terminal. `page.title()` recupera el título del documento y `page.url` informa la dirección actual.

Finalmente, `browser.close()` cierra el navegador de forma controlada.

#### Instrucciones

1. Inicie `server.py` en la Terminal 1.
2. No modifique `00_verificar_entorno.py`.
3. Ejecútelo desde la Terminal 2:

   ```bash
   python practicas/00_verificar_entorno.py
   ```

4. Observe que Chromium se abre automáticamente.
5. Compruebe que aparece el portal escolar.
6. Espere a que el navegador se cierre por sí mismo.

#### Resultado esperado

La terminal debe mostrar información semejante a:

```text
Título: Portal escolar de práctica
URL: http://127.0.0.1:8000/
Entorno listo.
```

#### Puede avanzar cuando

- Chromium se abre sin intervención manual.
- El portal es visible.
- La terminal muestra `Entorno listo.`.
- No aparece una excepción.

### Práctica 1. Navegar

Abre el portal, obtiene título y URL, y compara ejecución visible y headless.

Archivo: `practicas/01_navegar.py`.

Esta práctica reconstruye el flujo de la práctica 0 mediante espacios `TODO`. Sus elementos principales son:

```python
browser = playwright.chromium.launch(
    headless=False,
    slow_mo=300,
)
```

`launch()` inicia el navegador. Conviene experimentar cambiando `headless` y retirando `slow_mo` para observar que esas opciones afectan la visualización, no la lógica del bot.

```python
page = browser.new_page()
page.goto(PORTAL)
```

Estas instrucciones crean la pestaña y establecen el estado inicial de la automatización. En términos de RPA, `PORTAL` es un parámetro de configuración y no debería repetirse como texto literal en distintas partes del programa.

La salida en la terminal funciona como una primera forma de evidencia:

```python
print("Título:", page.title())
print("URL:", page.url)
```

#### Instrucciones

1. Abra `practicas/01_navegar.py` en VS Code.
2. Complete el `TODO 1` para iniciar Chromium con `headless=False` y `slow_mo=300`.
3. Complete el `TODO 2`: cree una página y navegue a `PORTAL`.
4. Complete el `TODO 3`: imprima título y URL.
5. Complete el `TODO 4`: cierre el navegador.
6. Guarde y ejecute:

   ```bash
   python practicas/01_navegar.py
   ```

7. Cambie temporalmente `headless=False` por `headless=True` y ejecute otra vez.
8. Explique qué cambió y qué permaneció igual. Restaure `headless=False`.

#### Resultado esperado

- En modo visible, Chromium abre el portal y luego se cierra.
- En modo headless, no aparece una ventana, pero la terminal presenta el mismo título y URL.

#### Puede avanzar cuando

- Puede explicar qué representan `browser` y `page`.
- El programa funciona tanto visible como headless.
- No necesita abrir un navegador antes de ejecutar el archivo.

### Práctica 2. Localizar elementos

Utiliza `get_by_role`, `get_by_label` y `get_by_test_id`.

Archivo: `practicas/02_localizadores.py`.

Un `Locator` no es el elemento en sí, sino una descripción reutilizable de cómo encontrarlo. Playwright vuelve a resolver esa descripción cuando realiza una operación.

```python
encabezado = page.get_by_role(
    "heading",
    name="Consulta de kárdex",
)
```

`get_by_role()` utiliza el rol accesible y, opcionalmente, el nombre que percibiría una persona usuaria. Es apropiado para encabezados, botones, enlaces y otros controles semánticos.

```python
campo = page.get_by_label("Matrícula")
```

`get_by_label()` relaciona un campo con su etiqueta visible. Es preferible a depender de una clase CSS utilizada únicamente para el diseño.

```python
boton = page.get_by_role("button", name="Buscar")
```

Este localizador expresa tanto el tipo como el propósito del elemento. Métodos como `is_visible()` y `text_content()` permiten consultar su estado o contenido.

En prácticas posteriores aparece:

```python
panel = page.get_by_test_id("result-panel")
```

`get_by_test_id()` utiliza un atributo incorporado deliberadamente para automatización. Es útil cuando un elemento no tiene un rol o nombre suficientemente distintivo.

#### Instrucciones

1. Abra `practicas/02_localizadores.py`.
2. Complete el `TODO 1` con un localizador por rol para el encabezado `Consulta de kárdex`.
3. Complete el `TODO 2` con un localizador por etiqueta para `Matrícula`.
4. Complete el `TODO 3` con un localizador por rol y nombre para el botón `Buscar`.
5. En el `TODO 4`, imprima el texto del encabezado y el estado visible del campo y del botón.
6. Guarde y ejecute:

   ```bash
   python practicas/02_localizadores.py
   ```

7. Modifique intencionalmente uno de los nombres, por ejemplo `Búsqueda`, y observe el error o el resultado.
8. Restaure el localizador correcto.

#### Resultado esperado

La terminal debe identificar el encabezado e informar que campo y botón están visibles.

#### Puede avanzar cuando

- Distingue un localizador de una acción.
- Puede justificar por qué se prefieren roles y etiquetas frente a coordenadas.
- Reconoce que el nombre del elemento debe corresponder a la interfaz.

### Práctica 3. Conservar evidencia

Genera capturas completas y de elementos específicos.

Archivo: `practicas/03_evidencia.py`.

`Path` permite construir rutas válidas en Windows, macOS y Linux:

```python
ROOT = Path(__file__).resolve().parents[1]
EVIDENCIAS = ROOT / "evidencias"
EVIDENCIAS.mkdir(exist_ok=True)
```

`__file__` representa el archivo Python actual. A partir de su ubicación se obtiene la raíz del proyecto, sin depender del directorio desde el que se ejecutó el comando.

La captura de página completa se realiza con:

```python
page.screenshot(
    path=EVIDENCIAS / "portal.png",
    full_page=True,
)
```

También puede capturarse únicamente un elemento:

```python
page.get_by_role(
    "heading",
    name="Consulta de kárdex",
).screenshot(path=EVIDENCIAS / "encabezado.png")
```

Las capturas son evidencia visual, pero no sustituyen los logs ni la validación del resultado. En un bot real deben generarse con un propósito definido, especialmente ante errores.

#### Instrucciones

1. Abra `practicas/03_evidencia.py`.
2. Complete el `TODO 1` para guardar una captura completa como `portal.png`.
3. Complete el `TODO 2` para capturar únicamente el encabezado en `encabezado.png`.
4. Guarde y ejecute:

   ```bash
   python practicas/03_evidencia.py
   ```

5. Abra la carpeta `evidencias/` desde el explorador de VS Code.
6. Compare ambas imágenes y explique cuándo sería útil cada una.

#### Resultado esperado

La carpeta `evidencias/` debe contener:

```text
portal.png
encabezado.png
```

#### Puede avanzar cuando

- Ambos archivos se abren correctamente.
- `portal.png` contiene la página completa.
- `encabezado.png` contiene solamente el encabezado.

### Práctica 4. Consultar un estudiante

Completa un formulario y diferencia una excepción de negocio.

Archivo: `practicas/04_consultar_estudiante.py`.

La matrícula se declara una sola vez:

```python
MATRICULA = "IAI0001"
```

Esto facilita cambiar la entrada y evita valores dispersos por el código. La interacción se construye con:

```python
page.get_by_label("Matrícula").fill(MATRICULA)
page.get_by_role("button", name="Buscar").click()
```

`fill()` reemplaza el contenido del campo y `click()` inicia la consulta. Playwright espera automáticamente que los elementos sean interactuables.

El resultado se recupera mediante:

```python
panel = page.get_by_test_id("result-panel")
texto = panel.inner_text()
```

`inner_text()` devuelve el texto visible consolidado del panel. Este dato permite distinguir:

- **éxito:** el estudiante existe y puede generarse su kárdex;
- **excepción de negocio:** el sistema funcionó correctamente, pero la matrícula no existe;
- **excepción técnica:** el portal no responde, el elemento cambió o la interacción no pudo completarse.

El reto de la práctica pide repetir el flujo con `IAI9999` para observar una excepción de negocio intencional.

#### Instrucciones

1. Abra `practicas/04_consultar_estudiante.py`.
2. Complete el `TODO 1` para llenar el campo con `MATRICULA`.
3. Complete el `TODO 2` para pulsar `Buscar`.
4. Complete el `TODO 3` utilizando `get_by_test_id("result-panel")`.
5. Complete el `TODO 4` para imprimir el contenido visible del panel.
6. Ejecute primero con `MATRICULA = "IAI0001"`.
7. Cambie la entrada por `IAI9999` y ejecute nuevamente.
8. Complete el `TODO 5` de modo que ambos casos se prueben en la misma ejecución.

   ```bash
   python practicas/04_consultar_estudiante.py
   ```

#### Resultado esperado

- `IAI0001` produce `ESTUDIANTE ENCONTRADO` y el nombre Ada Lovelace.
- `IAI9999` produce `EXCEPCIÓN DE NEGOCIO` y `Matrícula inexistente`.
- Ninguno de los dos casos debe terminar con una excepción de Python.

#### Puede avanzar cuando

- El programa prueba una matrícula válida y una inexistente.
- Puede explicar por qué `IAI9999` no representa un fallo técnico.
- El resultado se determina a partir de información presentada por la aplicación.

### Práctica 5. Descargar un kárdex

Utiliza `expect_download()` y guarda el archivo con un nombre controlado.

Archivo: `practicas/05_descargar_kardex.py`.

Las descargas son eventos asíncronos: el clic inicia el archivo, pero la descarga puede terminar después. Por ello se prepara la espera antes de pulsar el enlace:

```python
with page.expect_download() as download_info:
    page.get_by_role(
        "button",
        name="Descargar kárdex",
    ).click()
```

Al salir del bloque, Playwright proporciona el objeto de descarga:

```python
download = download_info.value
```

Después se controla el nombre y ubicación final:

```python
destino = DESCARGAS / f"kardex-{MATRICULA}.pdf"
download.save_as(destino)
```

No conviene asumir que el archivo apareció en la carpeta predeterminada del navegador. `save_as()` hace explícito el resultado del bot y facilita verificarlo posteriormente.

#### Instrucciones

1. Abra `practicas/05_descargar_kardex.py`.
2. Revise el flujo ya incluido: navegación, captura y búsqueda.
3. Complete el `TODO 1` creando el bloque `expect_download()` antes del clic.
4. Complete el `TODO 2` para obtener el objeto `Download`.
5. Complete el `TODO 3` y guarde el archivo en `descargas/` con la matrícula en el nombre.
6. Complete el `TODO 4` para informar la ruta final.
7. Guarde y ejecute:

   ```bash
   python practicas/05_descargar_kardex.py
   ```

8. Abra el PDF descargado y verifique que corresponde a `IAI0002`.

#### Resultado esperado

Debe crearse:

```text
descargas/kardex-IAI0002.pdf
```

El PDF debe abrirse y mostrar datos sintéticos de Alan Turing.

#### Puede avanzar cuando

- El archivo está en la carpeta controlada por el proyecto.
- El nombre incluye la matrícula.
- La terminal informa la ruta utilizada.
- Puede explicar por qué la espera se declara antes del clic.

### Práctica 6. Reto integrador

Reúne navegación, parámetros, validación, descarga, captura y resultado final.

Archivo: `practicas/06_reto_integrador.py`.

El reto combina las instrucciones anteriores dentro de una estructura de control:

```python
try:
    # Camino feliz y reglas de negocio
except Exception as error:
    # Evidencia y tratamiento del fallo técnico
finally:
    browser.close()
```

- `try` contiene el flujo normal y las decisiones previstas.
- `except` recibe errores técnicos inesperados; antes de terminar debería conservar una captura y explicar la causa.
- `finally` cierra el navegador tanto si hubo éxito como si ocurrió un error.

La decisión de negocio puede expresarse mediante el contenido del panel:

```python
if "Matrícula inexistente" in panel.inner_text():
    print("Excepción de negocio")
else:
    # Descargar el kárdex
```

Este ejemplo es deliberadamente sencillo. En una automatización posterior convendrá separar navegación, consulta, descarga y registro en funciones independientes, utilizar logs estructurados y definir excepciones más específicas.

#### Instrucciones

1. Abra `practicas/06_reto_integrador.py`.
2. Complete los `TODO` en orden; ejecute después de cada cambio importante.
3. Navegue al portal y consulte `MATRICULA`.
4. Localice el panel de resultado.
5. Guarde una captura cuyo nombre incluya la matrícula.
6. Si el estudiante existe, descargue el kárdex.
7. Si no existe, informe una excepción de negocio sin intentar la descarga.
8. Si ocurre una excepción de Python, guarde una captura completa antes de informar el error técnico.
9. Mantenga `browser.close()` dentro de `finally`.
10. Pruebe al menos estos casos:

    - `IAI0003`: camino feliz;
    - `IAI9999`: excepción de negocio;
    - detener temporalmente `server.py`: excepción técnica.

11. Reinicie el servidor después de la prueba técnica.

#### Resultado esperado

Para `IAI0003`:

```text
evidencias/resultado-IAI0003.png
descargas/kardex-IAI0003.pdf
```

Para `IAI9999` debe generarse evidencia del resultado, pero no un PDF nuevo. Si el servidor está detenido, el programa debe informar un error técnico y cerrar el navegador.

#### Puede considerar terminado el reto cuando

- Los tres escenarios tienen una salida comprensible.
- El camino feliz produce PDF y evidencia.
- La excepción de negocio no intenta descargar.
- El fallo técnico conserva contexto para diagnóstico.
- Chromium se cierra en todos los casos.

### Entrega del laboratorio

Entregue:

1. Los archivos `01_navegar.py` a `06_reto_integrador.py` completados.
2. La carpeta `evidencias/` con las capturas solicitadas.
3. La carpeta `descargas/` con los kárdex generados.
4. Un archivo `reflexion.txt` que responda brevemente:

   - ¿Qué diferencia existe entre una excepción técnica y una de negocio?
   - ¿Por qué son preferibles los localizadores semánticos?
   - ¿Por qué `expect_download()` se prepara antes del clic?
   - ¿Qué cambiaría para procesar una lista de matrículas?

### Relación entre las prácticas y un bot RPA

| Componente de RPA | Implementación en el laboratorio |
|---|---|
| Entrada | Variable `MATRICULA` y constante `PORTAL`. |
| Aplicación | Portal escolar ejecutado por `server.py`. |
| Interacción | `fill()`, `click()` y localizadores. |
| Regla de negocio | Determinar si la matrícula existe. |
| Resultado | PDF guardado en `descargas/`. |
| Evidencia | Capturas en `evidencias/` y mensajes en terminal. |
| Excepción de negocio | Matrícula inexistente. |
| Excepción técnica | Fallo de navegación, elemento ausente o descarga fallida. |
| Liberación de recursos | `browser.close()` dentro de `finally`. |

## Criterios de logro

- El bot usa localizadores semánticos; no coordenadas de pantalla.
- La matrícula es un parámetro y no está repetida en varias instrucciones.
- El bot reconoce éxito y matrícula inexistente.
- La descarga se guarda en `descargas/`.
- La captura se guarda en `evidencias/`.
- El navegador se cierra incluso si ocurre un error.
- La terminal informa el resultado de manera comprensible.

## Extensiones opcionales

1. Procesar una lista de matrículas.
2. Evitar descargas duplicadas.
3. Crear un archivo CSV con resultados.
4. Capturar evidencia solo en caso de error.
5. Reintentar una acción una sola vez.
6. Ejecutar en modo headless mediante un argumento.

## Reglas de seguridad

- No usar credenciales institucionales durante las prácticas.
- No sustituir los datos sintéticos por información estudiantil real.
- No automatizar sistemas productivos sin autorización.
- No incluir contraseñas, cookies o archivos descargados en Git.

## Soluciones

La edición docente contiene `soluciones_docente/` con implementaciones de referencia. El paquete `playwright_kardex_estudiantes.zip` excluye esa carpeta; puede entregarse antes de la sesión y compartir las soluciones al finalizar.
