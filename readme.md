# 📄 PDF Duplicate Checker

Aplicación web que permite **analizar archivos PDF** y detectar **nombres duplicados**, indicando **en qué página y línea** aparece cada repetición.

El sistema es capaz de procesar PDFs con **múltiples columnas** sin importar el formato, mostrando los resultados directamente en una interfaz web clara y amigable.

---

## 🚀 Funcionalidades

- 📂 Subida de archivos PDF desde el navegador
- 🔍 Análisis automático del contenido del PDF
- 👥 Detección de nombres duplicados
- 📍 Muestra página y línea de cada duplicado
- 📊 Resultados visualizados en una tabla
- 🔄 Indicador de carga durante el análisis
- 🪟 Modal informativo con el resultado final

---

## 🛠️ Tecnologías utilizadas

### Backend
- **Python 3**
- **FastAPI**
- **pdfplumber** (extracción de texto desde PDFs)
- **Uvicorn**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript (Fetch API)**

---

## 📁 Estructura del proyecto

```
pdf-duplicate-checker/
│
├── backend/
│   ├── app.py
│   ├── extractor.py
│   ├── detector.py
│   ├── requirements.txt
│   ├── uploads/
│   └── frontend/
│       └── index.html
│
├── .gitignore
└── README.md
```

---

## ▶️ Cómo ejecutar el proyecto localmente

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/KarlangaXZ/pdf-duplicate-checker.git
cd pdf-duplicate-checker
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r backend/requirements.txt
```

### 4️⃣ Ejecutar el servidor

```bash
cd backend
uvicorn app:app --reload
```

### 5️⃣ Abrir en el navegador

```
http://127.0.0.1:8000
```

---

## 📌 Uso de la aplicación

1. Abrir la aplicación en el navegador
2. Seleccionar un archivo PDF
3. Presionar **Analizar PDF**
4. Esperar el análisis
5. Visualizar resultados en pantalla

---

## 📷 Capturas de pantalla

*(Agrega aquí capturas del frontend mostrando el análisis y la tabla de resultados)*

---

## 🧠 Casos de uso

- Validación de listas de nombres
- Auditoría de documentos
- Control de duplicados en reportes
- Sistemas de facturación o RRHH

---

## 🔐 Notas de seguridad

- Los PDFs subidos no se almacenan permanentemente
- No se incluyen archivos PDF reales en el repositorio

---

## 👤 Autor

**Carlos Linares**  
Desarrollador Backend / Fullstack

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

---

⭐ Si este proyecto te resulta útil, no olvides darle una estrella en GitHub

