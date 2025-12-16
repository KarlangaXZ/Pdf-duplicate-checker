import pdfplumber

def extraer_lineas(pdf_path):
    resultados = []

    with pdfplumber.open(pdf_path) as pdf:
        for num_pagina, pagina in enumerate(pdf.pages, start=1):
            texto = pagina.extract_text()
            if not texto:
                continue

            lineas = texto.split("\n")

            for num_linea, linea in enumerate(lineas, start=1):
                resultados.append({
                    "pagina": num_pagina,
                    "linea": num_linea,
                    "texto": linea.strip()
                })

    return resultados
