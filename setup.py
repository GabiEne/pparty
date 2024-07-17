# setup.py

from PyInstaller.__main__ import run

# Options for PyInstaller
options = [
    '--onefile',            # Create a single file
    '--noconsole',          # Do not open a console window
    'app.py'                # Name of your Streamlit app script
]

run(options)
