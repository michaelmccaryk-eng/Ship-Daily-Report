# launcher.py — force normal mode on 8501, no Node dev server
import os, sys, threading, webbrowser

# ---- Turn OFF any dev mode before importing Streamlit ----
for k in (
    "STREAMLIT_DEV",
    "STREAMLIT_DEV_SERVER",
    "NODE_ENV",
    "STREAMLIT_GLOBAL_DEVELOPMENT_MODE",
    "BROWSER_SERVER_PORT",           # just in case
    "STREAMLIT_BROWSER_SERVER_PORT", # just in case
):
    os.environ.pop(k, None)

# Explicit config via env (belt & suspenders)
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_PORT"] = "8501"
os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

from streamlit.web.cli import main as st_main  # import AFTER env is set

def resource_path(rel_path: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.dirname(__file__), rel_path)

def open_browser(port: str):
    webbrowser.open(f"http://localhost:{port}", new=2)

if __name__ == "__main__":
    port = "8501"
    app_py = resource_path("app.py")

    # Open the browser shortly after server starts
    threading.Timer(1.2, open_browser, args=(port,)).start()

    # Run Streamlit with explicit flags to kill dev mode
    sys.argv = [
        "streamlit", "run", app_py,
        "--global.developmentMode=false",
        "--server.headless=true",
        "--server.port", port,
    ]
    st_main()
