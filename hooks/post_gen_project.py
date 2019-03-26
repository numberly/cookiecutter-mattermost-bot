import os


def remove_empty_files(dirpath):
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isdir(filepath):
            remove_empty_files(filepath)
        elif os.stat(filepath).st_size == 0 and filename != "__init__.py":
            os.remove(filepath)


remove_empty_files(".")

virtualenv = input("Create virtualenv? [y]:")
repository = input("Initialize Git repository? [y]:")

if virtualenv == "y" or not virtualenv:
    os.system("virtualenv -ppython3.7 .venv")
    requirements = input("Install requirements? [y]:")
    if requirements == "y" or not requirements:
        os.system(".venv/bin/pip install -r dev-requirements.txt")
if repository == "y" or not repository:
    os.system("git init .")
