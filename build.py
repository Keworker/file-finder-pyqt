import subprocess as Subprocess
import platform as Platform

if (Platform.system() == "Windows"):  # {
    Subprocess.run("pyinstaller Finder-chan-windows.spec")
# }
else:  # {
    pass
# }
