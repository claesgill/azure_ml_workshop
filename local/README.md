# Work from local machine
In this task you will learn how you can work with Azure ML from your local machine using the Azure ML SDK library.

The main goal is to learn about Azure ML and the Azure ML SDK, but continue reading if you would like to know more about the machinelearning algorithm and what it does.

## Char RNN
TODO

> :warning: It's important that you go trough the [Requirements](#requirements) section to be able to do any ot the tasks.

## Contents
1. [Requirements](#requirements)
    1. [Installation](#installation)
2. [Getting started](#getting-started)
3. [Create a config](#create-a-config)
4. [Upload dataset](#upload-dataset)
5. [Train a model](#train-a-model)
6. [Test trained model](#test-trained-model)
7. [Create own scripts](#create-own-scripts)
8. [Clean up](#clean-up)

## Requirements
> :information_source: It is recomended to use a virtual envrionment for python, but it is not required.

Before you start you need to check that you have the correct python version and all the packages you need.  
* Python v3.6.9 or higher
* pip3

You can check your python version in the terminal:  
```sh
python3 --version
```

### Installation
Copy and paste the following commands to install the requirements which includes all the packages you'll need for this workshop:  
```sh
cd local/
pip3 install -r requirements.txt
```

> :warning: This is only tested on Ubuntu 18.04. If you have issues you can try install the packages manually.

## Getting started
> :exclamation: Before you run the code it's important to note that all scripts include unfinished **todos**. These needs to be completed in each section to be able to run the script.

When you have verifyed that all [Requirements](#requirements) are in place, you can check the connection with Azure by running the following script. NB! Remember to fill in the **todos** first.   
```sh
python3 1_test_azure.py
```
This script will output your *Azure ML version*, *compute targets*, *datastores* and *datasets*.

Now that you've verified the connection proceed to section [Upload dataset](#upload-dataset).

## Create a config
We need the [`Workspace`](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace) class to consume our workspace on Azure Cloud. In the last section we used `Workspace.get()` method where we specified the `workspace_name` to get our workspace. Since we need to specify the workspace in each script, this becomes tedious over time. 
So, a solution is to use the `from_config` method instead to load the workspace from a config file. But before you can use that method you need to create the config using the `write_config` method.

Fill in the todos in `2_create_config.py`, and run your script to create the config:
```sh
python3 2_create_config.py
```

If your script worked, you should be able to locate a `.azureml/` folder containing a `.config.json` file.

#### Hints :bulb:
- Look for **3** todos.
- Check out the documentation for the [Workspace class](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace). 


## Upload dataset
In section [Datasets](https://github.com/claesgill/azure_ml_workshop#datasets) you uploaded a dataset manually into your workspace. This section you'll learn how  you can upload a dataset using the [Azure ML SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py). 

Fill in the todos in `3_upload_dataset.py`, and run your script:
```sh
python3 3_upload_dataset.py
```

If you don't get any error messages you can go to your workspace at [https://ml.azure.com/](https://ml.azure.com/), and verify that your dataset exists in the **Datasets** tab under Assets.

#### Hints :bulb:
- Look for **2** todos.
- Check out the documentation for [register datasets](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets#register-datasets).

## Train a model
In this task you will upload and run the training script(`train_char_rnn.py`). You can have a look at the script if you like, but it essentially trains a CharRNN model on the dataset you uploaded in the [Upload dataset](#upload-dataset) section.

The first thing you need to do is to set up a compute instance. If you don't have one already, you need to follow the steps in section [compute instance](https://github.com/claesgill/azure_ml_workshop/tree/issue_8_new_tasks#compute-instance) before you continue.

Fill in the todos in `4_deploy_to_azure.py`, and run your script:
```sh
python3 4_deploy_to_azure.py
```

If you script ran successfully, go to the [https://ml.azure.com]() verify that your training script has completed, and that you have a registered model named ?? .

#### Hints :bulb:
- Look for **2** todos.
- Check out the documentation for [Experiments](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py)
- Learn more about [Estimators](https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py) in the documentation

## Test trained model

TODO

#### Hints :bulb:
- Look for **XX** todos.
- 

## Create own scripts

TODO

#### Hints :bulb:
- Look for **XX** todos.
- 

## Clean up
TODO

## TODOs
- [ ] Add clean up script