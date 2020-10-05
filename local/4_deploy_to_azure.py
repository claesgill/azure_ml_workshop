import os, sys
from azureml.core import Workspace, Experiment, RunConfiguration, ScriptRunConfig
from azureml.train.estimator import Estimator
# from azureml.train.dnn import PyTorch
 
ws = Workspace.from_config()

# Creating an Estimator which is the environment for you experiment
estimator = Estimator(
    source_directory="./",
    entry_script="train_on_azure.py",
    script_params={
        "--filename": "", # TODO: Specify the same dataset_name you provided earlier 
        "--n_epochs": 10
        },
    compute_target="claes-testing",# TODO: Specify your compute target
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

# TODO: Create a "Experiment" and use the submit method to submit the "estimator" object
experiment = Experiment(workspace=ws, name="My experiment")
run = experiment.submit(config=estimator)
