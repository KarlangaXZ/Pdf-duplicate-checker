from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, UploadFile, File
from extractor import extraer_lineas
from detector import detectar_duplicados
import shutil
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/check-duplicates")
async def check_duplicates(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    registros = extraer_lineas(file_path)
    duplicados = detectar_duplicados(registros)

    if not duplicados:
        return {
            "status": "ok",
            "message": "No hay duplicidad en los nombres"
        }

    return {
        "status": "duplicados",
        "total": len(duplicados),
        "data": duplicados
    }
