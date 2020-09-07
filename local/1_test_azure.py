# external imports
import azureml.core
from azureml.core import Workspace
from azureml.core import ComputeTarget, Datastore, Dataset
# local imports
from src.config import Config
from src.colors import Colors
config = Config()
c = Colors()

# Load the workspace 
print("INFO: Loading workspace ...")
ws = Workspace.get(config.workspace_name)
print("{}Ready to use Azure ML '{}' to work with '{}'.{}".format(c.YELLOW, azureml.core.VERSION, ws.name, c.DEFAULT))

# Prints all the available compute targets
print("{}Compute Targets:{}".format(c.GREEN, c.DEFAULT))
for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print("{}\t{}: {}{}".format(c.BOLD, compute.name, compute.type, c.DEFAULT))
    
# Prints all the available datastores
print("{}Datastores:{}".format(c.GREEN, c.DEFAULT))
for datastore_name in ws.datastores:
    datastore = Datastore.get(ws, datastore_name)
    print("{}\t{}: {}{}".format(c.BOLD, datastore.name, datastore.datastore_type, c.DEFAULT))
    
# Prints all the available datasets
print("{}Datasets:{}".format(c.GREEN, c.DEFAULT))
for dataset_name in list(ws.datasets.keys()):
    dataset = Dataset.get_by_name(ws, dataset_name)
    print("{}\t{}{}".format(c.BOLD, dataset.name, c.DEFAULT))