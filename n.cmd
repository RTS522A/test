vssadmin.exe create shadow /for=c:
vssadmin list shadows
mklink /d vss \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\
dir vss\Temp /a /s
dir vss\PerfLogs /a /s
dir vss /a:-l /s > c:\temp\dir_list.txt

