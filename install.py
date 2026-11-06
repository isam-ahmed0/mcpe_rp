import os
import sys
import subprocess
from pathlib import Path

path = Path.home() / ".local" / "share" / "mcpe_rp"
print("Downloading....")
if not path.exists():
    subprocess.run(["git", "clone", "https://github.com/isam-ahmed0/mcpe_rp.git", str(path)], check=True)
sh_path = path / "install.sh"

print("Installing....")
subprocess.run(["sh", str(sh_path)], cwd=path, check=True)

print("Installed.\nRun mcpe_rp")