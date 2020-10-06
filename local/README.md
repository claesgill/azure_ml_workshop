# Work from local machine
In this task you will learn how you can work with Azure ML from your local machine using the Azure ML SDK library.

The main goal is to learn about Azure ML and the Azure ML SDK, but if would like to know more about the machinelearning algorithm and what it does, read the [Char RNN](#char-rnn) section.

> :warning: It's important that you go trough the [Requirements](#requirements) section to be able to do any of the tasks.

## Char RNN
The machinelearning that is used in this workshop is the Char RNN model, and is taken from [this reposetory](https://github.com/spro/char-rnn.pytorch). It is a multi-layer [Recurrent Neural Network (RNN)]() that uses the [GRU]() gating mechanism which is quite similar to the [LSTM](). 

Takes in a sequence of characters and trying to predict the next character in the sequence...

## Contents
1. [Requirements](#requirements)
    1. [Installation](#installation)
2. [Getting started](#getting-started)
3. [Create a config](#create-a-config)
4. [Upload dataset](#upload-dataset)
5. [Train a model](#train-a-model)
6. [Register a trained model](#register-a-trained-model)
7. [Test trained model](#test-trained-model)
8. [Create own scripts](#create-own-scripts)
9. [Clean up](#clean-up)

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
- Look for **3** todos
- Check out the documentation for the [Workspace class](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace). 


## Upload dataset
In section [Datasets](https://github.com/claesgill/azure_ml_workshop#datasets) you uploaded a dataset manually into your workspace. This section you'll learn how  you can upload a dataset using the [Azure ML SDK](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py). 

Fill in the todos in `3_upload_dataset.py`, and run your script:
```sh
python3 3_upload_dataset.py
```

If you don't get any error messages you can go to your workspace at [https://ml.azure.com/](https://ml.azure.com/), and verify that your dataset exists in the **Datasets** tab under Assets.

#### Hints :bulb:
- Look for **3** todos
- Check out the documentation for [register datasets](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets#register-datasets).

## Train a model
In this task you will upload and run the training script(`train_char_rnn.py`). You can have a look at the script if you like, or read more about what it does in the [Char RNN](#char-rnn) section. What it essentially does is that it trains a CharRNN model on the dataset you uploaded previously, and generates a trained model.

The first thing you need to do is to set up a compute instance. You need to follow the steps in section [compute instance](https://github.com/claesgill/azure_ml_workshop/tree/issue_8_new_tasks#compute-instance) before you continue.

Fill in the todos in `4_deploy_to_azure.py`, and run your script:
```sh
python3 4_deploy_to_azure.py
```

If your script finish with no errors, you can monitor that your experiment run successfully in the terminal. Another option is to monitor it in your ml-workspace ([https://ml.azure.com](https://ml.azure.com). See the below steps.

_NB! You may want to hit **refresh** frequently in each of the following steps_

1. Navigate to the **Experiments** page and choose your experiment 
2. Click your latest run and navigate to the **Outputs + logs** tab
3. Expand **azureml-logs** and wait for **70_driver_log.txt** to show and click it when it does. In this log-file you watch all the outputs from the  training-script and verify that everything ran successfully

#### Hints :bulb:
- Look for **3** todos
- Check out the documentation for [Experiments](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py)
- Learn more about [Estimators](https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py) in the documentation

## Register a trained model
In the previous section you may have noticed that your model was saved. However, it got saved in the container environment in Azure ML in witch don't make
it available to us. In order to make the model available to us we can use the `Model` class, and more specifically the `register` method to upload our model to Azure. Let's go ahead and do that!

Fill in the todos in `train_char_rnn.py` located in the `model` folder. Run the `4_deploy_to_azure.py` script afterwards:
```sh
python3 4_deploy_to_azure.py
```

To verify that your model was successfully uploaded, navigate to the **Models** page and you should see your model with the same name as you gave it.
You can click it to see more details.

#### Hints :bulb:
- Look for **1** todos
- The model i saved in the outputs folder in Azure ML
- Check out the documentation for the [Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py) class


## Test trained model
Now that you have trained and uploaded your model, it's time to test it and see how well it works. You can do this using the `5_generate.py` script.
The only thing you'll need to do is to download the model you registered earlier using the `Model` class and `download` method.

Fill in the todo in `5_generate.py` and run it:
```sh
python3 5_generate.py
```

TODO - how to validate

#### Hints :bulb:
- Look for **1** todo
- Check out the methods in the [Model](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py#methods) class documentation


## Create own scripts
TODO

#### Hints :bulb:
- Look for **XX** todos.
- 

## Clean up
TODO

## TODOs
- [ ] Add clean up script
- [x] Rewrite train_char_rnn.py with helpers as it was before..
