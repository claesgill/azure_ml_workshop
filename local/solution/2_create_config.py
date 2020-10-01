# TODO: Import Workspace from azureml core
from azureml.core import Workspace

# TODO: Create a Workspace instance to get your current workspace
ws = Workspace.get("wp-claes-ml")

# TODO: Use the write_config() method to get the workspace config on your local machine
ws.write_config()