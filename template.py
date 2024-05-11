import os
from pathlib import Path
import logging




logging.basicConfig(level=logging.INFO,format='[%(asctime)s] : %(message)s:')

project_name = "mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "test.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename =os.path.split(filepath)

    # First If conditions for creating directory
    if filedir!='':
        # We are settings exist_ok = True , to suppress os error if the folder is already exist.
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory:{filedir} and the file name is :{filename}")
    # Second IF conditions for Creating . files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file:{filepath}")
    # Else Display if already file exist
    else:
        logging.info(f"{filename} is  already exists")