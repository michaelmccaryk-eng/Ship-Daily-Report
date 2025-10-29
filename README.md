# 🚢 Ship Daily Report Tool

A lightweight Streamlit-based desktop app that helps Port Engineers and CQARs quickly create professional daily ship progress reports.

---

## 💡 Overview
This tool provides an easy-to-use interface for generating formatted `.docx` and `.txt` daily reports.  
It runs entirely offline on your local machine — no internet or coding knowledge required.

---

## 🖥️ How to Use
1. Download and unzip the package.
2. Double-click **`launcher.exe`**.
3. Your browser will open automatically at **http://localhost:8501**.
4. Fill out the form and click **Generate .docx** or **Download .txt**.

> ⚠️ If Windows SmartScreen or a firewall prompt appears, choose **“Run Anyway”** and **“Allow Access.”**

---

## 🧑‍💻 For Developers
### Run locally
```bash
pip install -r requirements.txt
python launcher.py
Build standalone .exe
powershell
Copy code
pyinstaller --onefile --noconsole --icon "app.ico" --add-data "app.py;." `
  --collect-all streamlit --collect-all docx --collect-all openpyxl --collect-all PIL `
  launcher.py
Executable will appear in dist\launcher.exe.

🗂️ Project Files
bash
Copy code
app.py              # Streamlit interface and report generator
launcher.py         # Opens Streamlit automatically in browser
requirements.txt    # Python dependencies
launcher.spec       # PyInstaller build spec
start-report.bat    # Optional quick-start script
🛡️ License & Contact
Developed by Michael McCary – Port Engineer / CQAR
For questions or collaboration, contact: michaelmccaryk-eng@users.noreply.github.com
