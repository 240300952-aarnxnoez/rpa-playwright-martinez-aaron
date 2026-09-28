"""Servidor del portal escolar sintético para el laboratorio."""

from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "app"

STUDENTS = {
    "IAI0001": "Ada Lovelace",
    "IAI0002": "Alan Turing",
    "IAI0003": "Grace Hopper",
}


def escape_pdf_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def build_pdf(enrollment: str, name: str) -> bytes:
    """Crea un PDF mínimo válido sin dependencias externas."""
    lines = [
        "KARDEX ACADEMICO - DATOS SINTETICOS",
        f"Matricula: {enrollment}",
        f"Estudiante: {name}",
        "Periodo: 2026-1",
        "RPA101  Automatizacion de procesos       95",
        "IAA202  Algoritmos para IA               92",
        "DAT210  Ingenieria de datos              89",
    ]
    commands = ["BT", "/F1 14 Tf", "72 750 Td"]
    for index, line in enumerate(lines):
        if index:
            commands.append("0 -28 Td")
        commands.append(f"({escape_pdf_text(line)}) Tj")
    commands.append("ET")
    stream = "\n".join(commands).encode("latin-1")

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]

    pdf = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{number} 0 obj\n".encode())
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")

    xref = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode())
    pdf.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref}\n%%EOF\n".encode()
    )
    return bytes(pdf)


class PortalHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def do_GET(self) -> None:
        path = unquote(urlparse(self.path).path)
        if path.startswith("/downloads/") and path.endswith(".pdf"):
            enrollment = Path(path).stem.removeprefix("kardex-").upper()
            name = STUDENTS.get(enrollment)
            if not name:
                self.send_error(404, "Matricula inexistente")
                return
            content = build_pdf(enrollment, name)
            self.send_response(200)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Disposition", f'attachment; filename="kardex-{enrollment}.pdf"')
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), PortalHandler)
    print(f"Portal disponible en http://{HOST}:{PORT}")
    print("Presione Ctrl+C para detenerlo.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()

