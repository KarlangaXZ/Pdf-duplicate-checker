from collections import defaultdict
import re

def detectar_duplicados(registros):
    nombres = defaultdict(list)

    for r in registros:
        texto = r["texto"]

        # Captura nombres tipo: "Chapman G", "Clark E Mrs"
        match = re.match(r"^[A-Z][a-zA-Z]+(\s+[A-Z])+", texto)

        if match:
            nombre = match.group().strip()
            nombres[nombre].append({
                "pagina": r["pagina"],
                "linea": r["linea"]
            })

    duplicados = {
        nombre: datos
        for nombre, datos in nombres.items()
        if len(datos) > 1
    }

    return duplicados

