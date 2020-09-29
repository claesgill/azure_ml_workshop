# external imports
import azureml.core
from azureml.core import Workspace, ComputeTarget, Datastore, Dataset
import os
# local imports
from src.config import Config; config = Config()
from src.colors import Colors; c      = Colors()

workspace_name = "wp-claes-ml"

# Load the workspace 
print("INFO: Loading workspace ...")
ws = Workspace.get(workspace_name)
print("{}Ready to use Azure ML '{}' to work with '{}'.{}".format(c.YELLOW, azureml.core.VERSION, ws.name, c.DEFAULT))

dataset_name       = input("Enter your dataset name:\n")
dataset_desciption = input("Enter dataset description:\n")

if dataset_name not in ws.datasets.keys():
    # TODO: Check if dataset exists
    # TODO: Save metadata?
    
    print("Uploading '{}' ...".format(dataset_name))
    try:
        # Uploading and registering dataset
        default_ds = ws.get_default_datastore()
        default_ds.upload_files(files=['./data/shakespeare.txt'], # Upload the diabetes csv files in /data
                                target_path='./',                 # Put it in a folder path in the datastore
                                overwrite=True,                   # Replace existing files of the same name
                                show_progress=True)

        shakespeare_data = Dataset.File.from_files(path=(default_ds, "./shakespeare.txt"))
        shakespeare_data.register(workspace=ws,
                            name=dataset_name,
                            description=dataset_desciption,
                            create_new_version=False)
        print("{}Success uploading dataset: '{}'{}".format(c.GREEN, dataset_name, c.DEFAULT))
    except Exception as e:
        print("{}An error occured while uploading dataset: '{}'{}".format(c.RED, dataset_name, c.DEFAULT))
        print(e)
else:
    print("{}Dataset '{}' already exists. Please provide another name.{}".format(c.RED, dataset_name, c.DEFAULT))