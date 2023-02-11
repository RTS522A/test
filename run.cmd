wmic cpu get /value
vssadmin.exe create shadow /for=c:
Dism /Capture-Image /ImageFile:"git.wim" /CaptureDir:"\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\" /Name:github
dir git.wim
