# external imports
import azureml.core
from azureml.core import Workspace, ComputeTarget, Datastore, Dataset
import os
# local imports
from src.config import Config; config = Config()
from src.colors import Colors; c      = Colors()


# Load the workspace 
print("INFO: Loading workspace ...")
ws = Workspace.from_config()

print("{}Ready to use Azure ML '{}' to work with '{}'.{}".format(c.YELLOW, azureml.core.VERSION, ws.name, c.DEFAULT))

# TODO: Give a name to your dataset and a description
dataset_name       = ""
dataset_desciption = ""


if dataset_name not in ws.datasets.keys():    
    print("Uploading '{}' ...".format(dataset_name))
    try:
        # Uploading and registering dataset
        default_ds = ws.get_default_datastore()
        default_ds.upload_files(files=['./data/shakespeare.txt'], # Upload the diabetes csv files from /data
                                target_path='./',                 # Put it in a folder path in the datastore
                                overwrite=True,                   # Replace existing files of the same name
                                show_progress=True)

        # Creating a Dataset File object to store the stream
        shakespeare_data = Dataset.File.from_files(path=(default_ds, "./shakespeare.txt"))

        # TODO: Use the .register method on 'shakespeare_data' to register your dataset to Azure ML
        


        print("{}Success uploading dataset: '{}'{}".format(c.GREEN, dataset_name, c.DEFAULT))
    except Exception as e:
        print("{}An error occured while uploading dataset: '{}'{}".format(c.RED, dataset_name, c.DEFAULT))
        print(e)
else:
    print("{}Dataset '{}' already exists. Please provide another name.{}".format(c.RED, dataset_name, c.DEFAULT))