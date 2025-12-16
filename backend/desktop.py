import webview
import threading
import uvicorn
import time

def start_server():
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        log_level="error",
        reload=False
    )

def start_desktop():
    # Espera a que FastAPI arranque
    time.sleep(1.5)

    webview.create_window(
        title="PDF Duplicate Checker",
        url="http://127.0.0.1:8000",
        width=1000,
        height=700,
        resizable=True
    )
    webview.start()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    start_desktop()
