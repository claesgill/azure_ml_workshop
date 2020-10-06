import os, sys
import azureml
from azureml.core import Workspace, Experiment
from azureml.train.estimator import Estimator
azureml._restclient.snapshots_client.SNAPSHOT_MAX_SIZE_BYTES = 10 * 10**9 # 10GB
 
ws = Workspace.from_config()


# Creating an Estimator which is the environment for your experiment
estimator = Estimator(
    # source_directory="./model/",
    source_directory="./model",
    entry_script="train_char_rnn.py",
    script_params={
        "--dataset": "claes", # TODO: Specify the same dataset_name you provided earlier 
        "--n_epochs": 10
        },
    compute_target="az-workshop-ci",# TODO: Specify your compute target
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
experiment = Experiment(workspace=ws, name="my-experiment")
run = experiment.submit(config=estimator)
run.wait_for_completion(show_output=True)
