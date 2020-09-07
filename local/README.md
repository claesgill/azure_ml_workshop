# Work from local machine
In this task you will learn how you can work with Azure ML from your local machine using the Azure ML SDK library.

> :warning: It's important that you go trough the [Requirements](#requirements) section to be able to complete this task.

## Contents
*TODO*

## Requirements
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
When you have verifyed that all reqirements are in place you can check the connection with Azure by running:  
```sh
python3 1_test_azure.py
```
This script will output you *Azure ML version*, your *compute targets*, *datastores* and *datasets*.

Now that you've verified the connection proceed to section [Upload dataset](#upload-dataset).

## Upload dataset
In a section [Datasets]() you uploaded a dataset manually into the `ml-aisl` workspace. This section you'll show you how you can upload a dataset using the [Azure ML SDK]().


## Train a model

