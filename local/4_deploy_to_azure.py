import os, sys
from azureml.core import Workspace, Experiment, RunConfiguration, ScriptRunConfig
from azureml.train.estimator import Estimator
# from azureml.train.dnn import PyTorch

# TODO: Specify the same dataset_name you provided earlier, and give you experiment a name
dataset_name      = ""
experiment_name   = ""
entry_script_name = 'train_on_azure.py'

ws = Workspace.from_config()

# Creating an Estimator which is the environment for you experiment
estimator = Estimator(
    source_directory='./',
    entry_script=entry_script_name,
    script_params={
        '--filename': 'shakespare_1',
        '--n_epochs': 10
        },
    compute_target='claes-testing',
    pip_packages=[
        "azureml-core",
        "azureml-dataprep",
        "azureml-train",
        "pandas",
        "torch",
        "torchvision",
        "tqdm",
        "Unidecode"
    ]
)

# TODO: Create a 'Experiment' and use the submit method to submit the 'estimator' object
experiment = Experiment(workspace=ws, name=experiment_name)
run = experiment.submit(config=estimator)
