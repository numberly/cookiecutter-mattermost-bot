import os

virtualenv = input("Create virtualenv? [y]:")
repository = input("Initialize Git repository? [y]:")

if virtualenv == "y" or not virtualenv:
    os.system("virtualenv -ppython3.7 .venv")
    requirements = input("Install requirements? [y]:")
    if requirements == "y" or not requirements:
        os.system(".venv/bin/pip install -r dev-requirements.txt")
if repository == "y" or not repository:
    os.system("git init .")
