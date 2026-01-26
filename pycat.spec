# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['pycat_entry.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/keywords.py', '.'),
        ('src/__init__.py', '.'),
        ('src/main.py', '.')
    ],
    hiddenimports=['keywords'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pycat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
