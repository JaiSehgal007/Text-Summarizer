# project template creation
import os
from pathlib import Path
import logging # to log all ingormation

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # to create the logging screen

project_name="testSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    # we will be using this folder when we will be doing the ci/cd deployment, 
    # so what it will do on the commit it will direcly take to the cloud
    # git keep is the hiiden file, to be deleted later
    f"src/{project_name}/__inti__.py", # creating a constructer file inside it __init__
    # we need the constructer file as, line we want to write something to import from 
    # for these import operation, we need this folder as a local package, and if we want 
    # to install as a local package at that time thsi constructer file is needed 
    # whenever this constructer file is present that folder will be considered as a local package
    f"src/{project_name}/components/__inti__.py",
    f"src/{project_name}/utils/__inti__.py",
    f"src/{project_name}/utils/common.py", #common file is used to write all the utility
    f"src/{project_name}/logging/__inti__.py",
    f"src/{project_name}/config/__inti__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", # it contain all model related parameters
    "app.py",
    "main.py", 
    # we will build a docker image of the source code and we will do the deployment
    # of the image in our pc to machine in our AWS, so thats why we are using docker
    "Dockerfile",
    "requirements.txt",
    "setup.py", # to do the local pacakage setup
    "research/trials.ipynb" # this will contain all the notebook experiments
]

for filepath in list_of_files:
    # converting the file path to the specified os format, if these are not handled it 
    # throw error while we switch from windows to linux, to handle it we have path library
    filepath = Path(filepath)
    # seperating out folders and file
    filedir,filename = os.path.split(filepath)

    if(filedir!=""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass # just passing as we are not doing anything right now in the file
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename}  is already existing ")


# ṇow runnign this file in terminal as : python template.py