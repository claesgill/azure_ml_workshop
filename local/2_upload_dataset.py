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

# Check if dataset exists
print(ws.datasets)
# datastore = Datastore(workspace=ws, name="workspacefilestore")
# print(datastore)

# Download dataset from Oslo Bysykkel
bysykkel_url  = "https://data.urbansharing.com/oslobysykkel.no/trips/v1/2020/08.csv"
bysykkel_data = Dataset.Tabular.from_delimited_files(bysykkel_url)
bysykkel_data.register(workspace=ws,
                       name="oslo_bysykkel",
                       description="Oslo Bysykkel data",
                       create_new_version=False)

# dummy = Dataset.File.from_files(path="data/dummy.csv")
# print(dummy)
# dataset = Dataset(definition="New dataset", workspace=ws)
# print(dataset)
# Create a dataset and save it

# Upload our created dataset
