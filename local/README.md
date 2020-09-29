# Work from local machine
In this task you will learn how you can work with Azure ML from your local machine using the Azure ML SDK library.

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
> :bulb: Look for **3** todos in `2_create_config`

We need the [`Workspace`](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace) class to consume our workspace on Azure Cloud. 
In the last section we used `Workspace.get()` method where we specified the `workspace_name` to get our workspace. Since we need to specify the workspace in each script, this becomes tedious over time. 
So, a solution is to use the `from_config` method instead to load the workspace from a config file. But before you can use that method you need to create the config using the `write_config` method.

Fill in the todos in `2_create_config`, and run your script to create the config:
```sh
python3 2_create_config.py
```

To verify that your script works, you should be able to locate a `.azureml/` folder containing a `.config.json` file.

#### Hints
- Check out the documentation for the [Workspace class](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py#workspace). 


## Upload dataset
> :bulb: Look for **XX** todos

In a section [Datasets]() you uploaded a dataset manually into the `ml-aisl` workspace. This section you'll show you how you can upload a dataset using the [Azure ML SDK](). You can have a look at the code in `2_upload_dataset.py` to see how it's done. Feel free to ask if you have any questions!  

To upload the dataset you need to run
```sh
python3 2_upload_dataset.py
```
in terminal.

Running this script will prompt you to insert a **dataset name** and a **dataset description**. It is imporatant that you pick an easy but unique dataset name as you need to use it for later tasks. 

## Train a model
> :bulb: Look for **XX** todos

To upload and train the model run
```sh
python3 deploy_to_azure.py
```
in terminal.

Here you will need to provide the same **dataset name** that you specified before, and a name for your **experiment**.

## Test trained model
> :bulb: Look for **XX** todos

TODO

## Create own scripts
> :bulb: Look for XX todos

TODO

## Clean up
TODO

## TODOs
- [ ] Add clean up script ?