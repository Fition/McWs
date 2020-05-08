# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['check.py', 'cmdarg.py', 'init.py', 'main.py', 'packages.py', 'please_tell.py', 'restart.py', 'send_message.py', 'saysay.py', 'take_water.py'],
             pathex=['function', 'ForQQ', 'agent', 'image', 'nbtread', 'G:\\python\\projects\\minecraft'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='check',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
