# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['pycat_entry.py'],
    pathex=[],
    binaries=[],  # Add Python DLL here if needed
    datas=[('src/*.py', '.')],
    hiddenimports=['keywords'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Collect Python DLL
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Make sure binaries include Python DLL
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # This includes Python DLL
    a.zipfiles,
    a.datas,
    [],
    name='pycat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Compress to reduce size
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Keep console for CLI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None  # Add icon path if you have one
)
