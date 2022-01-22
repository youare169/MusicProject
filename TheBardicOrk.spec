# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['TheBardicOrk.py'],
             pathex=['C:\\Users\\Isaac\\PycharmProjects\\AudioMixer'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('Victory Sound Effect.wav','C:\\Users\\Isaac\\PycharmProjects\\AudioMixer\\resources\\Victory Sound Effect.wav', "DATA")]
a.datas += [('Chad.gif','C:\\Users\\Isaac\\PycharmProjects\\AudioMixer\\resources\\Chad.gif', "DATA")]
a.datas += [('NonCombat.gif','C:\\Users\\Isaac\\PycharmProjects\\AudioMixer\\resources\\NonCombat.gif', "DATA")]
a.datas += [('Pleb.gif','C:\\Users\\Isaac\\PycharmProjects\\AudioMixer\\resources\\Pleb.gif', "DATA")]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)



exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='TheBardicOrk',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
