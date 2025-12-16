from collections import defaultdict
import re

def detectar_duplicados_stream(registros):
    nombres = defaultdict(list)

    for r in registros:
        match = re.match(r"^[A-Z][a-zA-Z]+(\s+[A-Z])+", r["texto"])
        if match:
            nombre = match.group().strip()
            nombres[nombre].append({
                "pagina": r["pagina"],
                "linea": r["linea"]
            })

    return {
        nombre: datos
        for nombre, datos in nombres.items()
        if len(datos) > 1
    }


