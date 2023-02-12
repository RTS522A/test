vssadmin.exe create shadow /for=c:
vssadmin list shadows
mklink /d vss \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
dir /a /s
