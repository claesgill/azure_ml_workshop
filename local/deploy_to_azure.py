import os, sys
from azureml.core import Workspace, Experiment, RunConfiguration, ScriptRunConfig
from azureml.train.dnn import PyTorch

ws = Workspace.get(name='ml-aisl')


estimator = PyTorch(
    source_directory='./',
    entry_script='train_on_azure.py',
    script_params={
        'filename': 'shakespare_1',
        '--n_epochs': 10
        },
    compute_target='local'
)

# expertiment_run_config = RunConfiguration()
# src = ScriptRunConfig(
#     source_directory='./',
#     script='train_on_azure.py',
#     run_config=expertiment_run_config
# )

experiment = Experiment(workspace=ws, name='shakespare-experiement') # TODO: Make name dynamic from different users

run = experiment.submit(config=estimator)
