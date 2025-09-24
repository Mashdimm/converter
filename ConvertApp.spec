# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icons.ico', '.'),                      # Иконка
        ('*.ttf', '.'),                          # Шрифты, если есть
        ('*.ui', '.'),                           # UI-файлы, если используешь их напрямую
    ],
    hiddenimports=[
        'googletrans', 'decimal', 'PyQt6.QtGui', 'PyQt6.QtWidgets',
        'PyQt6.QtCore', 're', 'csv', 'win32com.client',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'tkinter', 'unittest', 'test', 'email', 'pydoc', 'matplotlib', 'PIL.ImageTk'
    ],
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
    name='ConvertApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,             # Отключаем консоль
    icon='icons.ico'           # Иконка (по желанию)
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ConvertApp'
)