# -*- mode: python -*-

block_cipher = None

a = Analysis(['C:\\Users\\Raptorsw0rd\\Dropbox\\map_stuff\\map_sources\\newpacktesting\\findall.py'],
             pathex=['C:\\Users\\Raptorsw0rd\\AppData\\Local\\Programs\\Python\\Python36-32\\Scripts'],
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
          name='BSPZIP-Toe',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
		  icon='C:\\Users\\Raptorsw0rd\\Documents\\github\\BSPZIP-Toe\\icon.ico',
          console=False )
