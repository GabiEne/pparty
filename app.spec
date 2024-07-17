# app.spec

# -*- mode: python ; coding: utf-8 -*-

import glob
import os
from PyInstaller.utils.hooks import copy_metadata

# Copy metadata for streamlit and its dependencies
streamlit_metadata = copy_metadata('streamlit')
pandas_metadata = copy_metadata('pandas')
openpyxl_metadata = copy_metadata('openpyxl')

# Collect all metadata directories
all_metadata = streamlit_metadata + pandas_metadata + openpyxl_metadata

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('BD_GabiDOBRITA.xlsx', '.'),
        ('streamlit_app.py', '.'),
    ] + all_metadata,
    hiddenimports=['streamlit', 'pandas', 'openpyxl'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
