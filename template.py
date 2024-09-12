import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

#################################
# Define project_name2 for templates and static
project_name2 = "templates"
project_name3 = "static"
project_name4 = "notebook"
###############################################




list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    f"{project_name2}/index.html",  # templates directory
    f"{project_name3}/css/styles.css",  # static directory for CSS
    f"{project_name3}/js/scripts.js",  # static directory for JS
    f"{project_name4}/1 . EDA STUDENT PERFORMANCE (1).ipynb",  # static directory for notebook
    f"{project_name4}/2. MODEL TRAINING.ipynb",  # static directory for notebook
    #f"{project_name4}/1_EDA_US_visa.ipynb",  # static directory for notebook
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")