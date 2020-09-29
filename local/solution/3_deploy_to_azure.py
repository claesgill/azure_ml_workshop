import os, sys
from azureml.core import Workspace, Experiment, RunConfiguration, ScriptRunConfig
from azureml.train.dnn import PyTorch
from azureml.train.estimator import Estimator

# TODO: fill inn here
dataset_name      = input("Enter your dataset name:\n")
experiment_name   = input("Enter a experient name:\n")
entry_script_name = 'train_on_azure.py'

# TODO: Make need  to fill in
ws = Workspace.get(name='wp-claes-ml')

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

# Submit experiment
experiment = Experiment(workspace=ws, name=experiment_name) # TODO: Make name dynamic from different users
run = experiment.submit(config=estimator)
