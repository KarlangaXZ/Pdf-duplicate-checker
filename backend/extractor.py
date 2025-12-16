import pdfplumber

def extraer_lineas_stream(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for num_pagina, pagina in enumerate(pdf.pages, start=1):
            texto = pagina.extract_text()
            if not texto:
                continue

            for num_linea, linea in enumerate(texto.split("\n"), start=1):
                yield {
                    "pagina": num_pagina,
                    "linea": num_linea,
                    "texto": linea.strip()
                }

