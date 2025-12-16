# 📄 PDF Duplicate Checker

Web application that allows you to **analyze PDF files** and detect **duplicate names**, indicating **the page and line** where each repetition appears.

The system is capable of processing PDFs with **multiple columns**, regardless of their layout, displaying the results directly in a clean and user-friendly web interface.

---

## 🚀 Features

* 📂 Upload PDF files from the browser
* 🔍 Automatic analysis of PDF content
* 👥 Duplicate name detection
* 📍 Displays page and line for each duplicate
* 📊 Results displayed in a table
* 🔄 Loading indicator during analysis
* 🪟 Informational modal with the final result

---

## 🛠️ Technologies Used

### Backend

* **Python 3**
* **FastAPI**
* **pdfplumber** (text extraction from PDFs)
* **Uvicorn**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript (Fetch API)**

---

## 📁 Project Structure

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

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/KarlangaXZ/pdf-duplicate-checker.git
cd pdf-duplicate-checker
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4️⃣ Run the server

```bash
cd backend
uvicorn app:app --reload
```

### 5️⃣ Open in your browser

```
http://127.0.0.1:8000
```

---

## 📌 How to Use the Application

1. Open the application in your browser
2. Select a PDF file
3. Click **Analyze PDF**
4. Wait for the analysis to complete
5. View the results on the screen


## 🧠 Use Cases

* Name list validation
* Document auditing
* Duplicate control in reports
* Billing or HR systems

---

## 🔐 Security Notes

* Uploaded PDFs are not stored permanently
* No real PDF files are included in the repository

---

## 👤 Author

**Carlos Linares**
Backend / Fullstack Developer

---

## 📄 License

This project is distributed under the **MIT** license.

---

⭐ If you find this project useful, don’t forget to give it a star on GitHub
