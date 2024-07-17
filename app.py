import sys
import subprocess
import pandas as pd
import os
import webbrowser
import time
import socket

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import openpyxl
except ImportError:
    install("openpyxl")
    import openpyxl

# Adjust path for executable
application_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__))
file_path = os.path.join(application_path, 'BD_GabiDOBRITA.xlsx')
data = pd.read_excel(file_path, sheet_name='0, Baza de date_iunie 2024')
localities = data['Valori'].unique()


streamlit_app_path = os.path.join(application_path, "streamlit_app.py")

def open_browser():
    time.sleep(5)
    webbrowser.open_new("http://localhost:8501")

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def main():
    try:
        streamlit_proc = subprocess.Popen([sys.executable, "-m", "streamlit", "run", streamlit_app_path])
        while not is_port_in_use(8501):
            time.sleep(1)
        open_browser()
        streamlit_proc.wait()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if streamlit_proc:
            streamlit_proc.terminate()

if __name__ == "__main__":
    if not is_port_in_use(8501):
        main()
    else:
        print("Server already running.")
