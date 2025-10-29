@echo off
setlocal
cd /d %~dp0

REM --- Activate your Python venv ---
call ".venv\Scripts\activate.bat"

REM --- Launch the Streamlit app ---
start "" http://localhost:8501
python -m streamlit run app.py --server.headless true --server.port 8501
