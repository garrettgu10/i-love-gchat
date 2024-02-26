import re
import subprocess
import os

# https://packaging.python.org/en/latest/specifications/name-normalization/
def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

for req in requirements:
    [name, version] = req.split("==")
    name = normalize(name)
    path = "packages/" + name
    if os.path.isdir(path):
        continue
    subprocess.run(["mkdir", "-p", path], check=True)
    subprocess.run(["/Users/garrett/.venv-pyodide/bin/pip", "install", name + "==" + version, "-t", path, "--no-deps"], check=True)
