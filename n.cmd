vssadmin.exe create shadow /for=c:  
mklink /d d:\a\temp\temp\vss \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
dir "d:\a\temp\temp\vss" /a
