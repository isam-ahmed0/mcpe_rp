import os
import sys
import subprocess
from pathlib import Path

path = Path.home() / ".local" / "share" / "mcpe_rp"
print("Fething....")
if not path.exists():
    print("Not isntalled\nInstall using\ncurl -fsSL https://raw.githubusercontent.com/isam-ahmed0/mcpe_rp/refs/heads/dev/install.py | python3")
    sys.exit(1)

print("Updating..")
subprocess.run(["git", "pull"], cwd=path, check=True)

print("Updating modules...")
venv_python = path / ".venv" / "bin" / "python"
subprocess.run([str(venv_python), "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"], cwd=path, check=True)

print("Done. run mcpe_rp")