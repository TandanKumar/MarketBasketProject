import os
from pathlib import Path

package_name = "MARKET_BASKET_PROJECT"

list_of_files = [

 "requirements.txt",
 "app.py",
 "Dockerfile",
 ".dockerignore",
 ".github\workflows\main.yaml",
 "setup.py",
  f"{package_name}/__init__.py", 
   f"{package_name}/exception/__init__.py",
   f"{package_name}/logger/__init__.py",
   f"{package_name}/pipeline/__init__.py",
   f"{package_name}/pipeline/pipeline.py",
   f"{package_name}/config/__init__.py",
   f"{package_name}/config/configuration.py",
   f"{package_name}/entity/__init__.py",
   f"{package_name}/entity/config_entity.py",
   f"{package_name}/entity/artifact_entity.py",
   f"{package_name}/component/__init__.py",
   f"{package_name}/component/data_ingestion.py",
   f"{package_name}/component/data_transformation.py",
   f"{package_name}/component/data_validation.py",
   f"{package_name}/component/data_evaluation.py",
   f"{package_name}/component/model_pusher.py",
   f"{package_name}/component/model_trainer.py",
   f"{package_name}/util/util.py",
   f"{package_name}/util/__init__.py",
   f"{package_name}/constant/__init__.py",
   "config/config.yaml",
   "config/model.yaml",
   "config/schema.yaml"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            