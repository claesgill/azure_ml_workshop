# Azure ML Workshop :test_tube: 

## Contents
1. [Getting started](#getting_started)
2. [Compute instance](#compute-instance)
    i. [Create a compute instance](#create-a-compute-instance)
    ii. 

## Getting started
1. Login to the [Azure Portal](https://portal.azure.com/)
2. Check that `AI Studentlab` is available in *Subscription*
    - Go to *Resources* and choose `ml_aisl`
    - Click **Launch Now** to go to Azure Machine Learning studio. Alternatively you can open [Azure ML](https://ml.azure.com), where you need to sign with the following selected:  
        * **Directory**: Skatteetaten
        * **Subscription**: AI Studentlab
        * **Machine Learning workspace**: ml-aisl

Feel free to explore Azure ML Studio.


## Compute instance
**TODO: Explenation here**

### Create a compute instance
1. Navigate to *Compute* and chose *Compute instances*. Then create a **new** compute instance.

2. Fill in the following:  
    * **Compute name**: <your_name>workshop
    * **Region**: westeurope 
    * **Virtual machine type**: CPU (Central Processing Unit)
    * **Virtual machine size**: Standard D1

> :warning: You need to provide the correct information otherwise you may encounter problems later in this workshop.

3. Make sure your information is correct before you click **create**.

### Clone repo into compute instance
You can perform most asset management tasks to set up your environment in the Studio interface, but it's also important to be able to script configuration tasks to make them easier to repeat and automate.

1. In [Azure Machine Learning studio](https://ml.azure.com/), on the **Compute** page for your workspace, view the **Compute Instances** tab, and if necessary, click **Refresh** periodically until the compute instance you created in the previous lab has started.

2. Refresh the Azure Machine Learning studio web page in your browser to ensure your authenticated session has not expired. Then click your compute instance's Jupyter link to open **Jupyter** Notebooks in a new tab. If prompted, sign in using the Microsoft account associated with your Azure subscription.

3. In the notebook environment, create a new **Terminal**. This will open a new tab with a command shell.

4. The Azure Machine Learning SDK is already installed in the compute instance image, but it's worth ensuring you have the latest version, with the optional packages you'll need in this course; so enter the following command to update the SDK packages:
```sh
pip install --upgrade azureml-sdk[notebooks,automl,explain]
```

You may see some warnings as the package dependencies are installed. You can ignore these.

>More Information: For more details about installing the Azure ML SDK and its optional components, see the Azure ML SDK Documentation.

5. Next, run the following commands to change the current directory to the Users directory, and retrieve the notebooks you will use in the labs for this course:

```sh
cd Users
git clone https://github.com/shoresh57/AI-ML-Workshop-Azure
```

6. After the command has completed, close the terminal tab and view the home page in your Jupyter notebook file explorer. Then open the Users folder - it should contain an AI-ML-Workshop-Azure folder, containing the files you will use in the rest of this lab.

7. In the Users/AI-ML-Workshop-Azure/DataSienceSolutionAzure folder, open the 01B - Intro to the Azure ML SDK.ipynb notebook. Then read the notes in the notebook, running each code cell in turn.

8. When you have finished running the code in the notebook, on the File menu, click Close and Halt to close it and shut down its Python kernel. Then close all Jupyter browser tabs.

9. In Azure Machine Learning studio, on the Compute page, select your compute instance and click Stop to shut it down.

## Datasets (needs to go after Compute Instance-section)
Working with machine learning usually requires big chunks of data ...

1. In the *Studio* interface, view the Datastores page. Your Azure ML workspace already includes two datastores based on the Azure Storage account that was created along with the workspace. These are used to store notebooks, configuration files, and data.

2. In the *Studio* interface, view the Datasets page. Datasets represent specific data files or tables that you plan to work with in Azure ML.

3. Create a new dataset from web files, using the following settings:
    * **Basic Info**:
        - **Web URL**: [https://aka.ms/diabetes-data](https://aka.ms/diabetes-data)
        - **Name**: diabetes dataset (be careful to match the case and spacing)
        - **Dataset type**: Tabular
        - **Description**: Diabetes data
    * **Settings and preview**:
        - **File format**: Delimited
        - **Delimiter**: Comma
        - **Encoding**: UTF-8
        - **Column headers**: Use headers from first file
        - **Skip rows**: None
    * **Schema**:
        - Include all columns other than Path
        - Review the automatically detected types
    * **Confirm details**:
        - Do **not** profile the dataset after creation

4. After the dataset has been created, open it and view the Explore page to see a sample of the data. This data represents details from patients who have been tested for diabetes, and you will use it in many of the subsequent labs in this course.

5. Go and run notebook `:shrug:` to see the data frames?

## Train and register models
*TODO: Create a notebook for this!*

In this task, you'll use code in a notebook to run training scripts as Azure Machine Learning experiments.

1. In Azure Machine Learning studio, view the **Compute** page for your workspace; and on the **Compute Instances** tab, start your compute instance.

2. When the compute instance is running, refresh the Azure Machine Learning studio web page in your browser to ensure your authenticated session has not expired. Then click the *Jupyter* link to open the Jupyter home page in a new browser tab.

3. In the Jupyter home page, in the **Users/AI-ML-Workshop-Azure/DataSienceSolutionAzure** folder, open the **03B - Training Models.ipynb notebook**. Then read the notes in the notebook, running each code cell in turn.

4. When you have finished running the code in the notebook, on the **File** menu, click **Close and Halt** to close it and shut down its Python kernel. Then close all Jupyter browser tabs.

5. In Azure Machine Learning studio, on the **Compute** page, select your compute instance and click **Stop** to shut it down.

## Pipeline
**TODO: Create notebook**

**Why build pipelines?**
With pipelines, you can optimize your workflow with simplicity, speed, portability, and reuse. When building pipelines with Azure Machine Learning, you can focus on what you know best — machine learning — rather than infrastructure.

Using distinct steps makes it possible to rerun only the steps you need as you tweak and test your workflow. Once the pipeline is designed, there is often more fine-tuning around the training loop of the pipeline. When you rerun a pipeline, the execution jumps to the steps that need to be rerun, such as an updated training script, and skips what hasn't changed. The same paradigm applies to unchanged scripts and metadata.

With Azure Machine Learning, you can use distinct toolkits and frameworks for each step in your pipeline. Azure coordinates between the various compute targets you use so that your intermediate data can be shared with the downstream compute targets easily

[image]

[other_image]

*azureml-pipeline-steps package*

Contains pre-built steps that can be executed in an Azure Machine Learning Pipeline.

Azure ML Pipeline steps can be configured together to construct a Pipeline, which represents a shareable and reusable Azure Machine Learning workflow. Each step of a pipeline can be configured to allow reuse of its previous run results if the step contents (scripts and dependencies) as well as inputs and parameters remain unchanged

Common kinds of step in an Azure Machine Learning pipeline include:

* PythonScriptStep: Runs a specified Python script.

* EstimatorStep: Runs an estimator.

* DataTransferStep: Uses Azure Data Factory to copy data between data stores.

* DatabricksStep: Runs a notebook, script, or compiled JAR on a databricks cluster.

* AdlaStep: Runs a U-SQL job in Azure Data Lake Analytics.

https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps?view=azure-ml-py

*PipelineData class*
Represents intermediate data in an Azure Machine Learning pipeline.

Data used in pipeline can be produced by one step and consumed in another step by providing a PipelineData object as an output of one step and an input of one or more subsequent steps.

**Azure ML pipelines**
An Azure Machine Learning pipeline is an independently executable workflow of a complete machine learning task. Subtasks are encapsulated as a series of steps within the pipeline. An Azure Machine Learning pipeline can be as simple as one that calls a Python script, so may do just about anything. Pipelines should focus on machine learning tasks such as:

* Data preparation including importing, validating and cleaning, munging and transformation, normalization, and staging

* Training configuration including parameterizing arguments, filepaths, and logging / reporting configurations

* Training and validating efficiently and repeatedly. Efficiency might come from specifying specific data subsets, different hardware compute resources, distributed processing, and progress monitoring

* Deployment, including versioning, scaling, provisioning, and access control

Independent steps allow multiple data scientists to work on the same pipeline at the same time without over-taxing compute resources. Separate steps also make it easy to use different compute types/sizes for each step.

### Creating a pipeline
In this task, you'll create a pipeline to train and register a model.

What we want to achieve in this is .... *TODO*

1. In Azure Machine Learning studio, view the Compute page for your workspace; and on the Compute Instances tab, start your compute instance.

2. When the compute instance is running, refresh the Azure Machine Learning studio web page in your browser to ensure your authenticated session has not expired. Then click the Jupyter link to open the Jupyter home page in a new browser tab.

3. In the Jupyter home page, in the Users/AI-ML-Workshop-Azure/DataSienceSolutionAzure folder, open the 06A - Creating a Pipeline.ipynb notebook. Then read the notes in the notebook, running each code cell in turn.

4. When you have finished running the code in the notebook, on the File menu, click Close and Halt to close it and shut down its Python kernel. Then close all Jupyter browser tabs.

5. In Azure Machine Learning studio, on the Compute page, select your compute instance and click Stop to shut it down.

## Train from local machine
*TODO*
### Requirements

* Python v3.6.9 or higher
* pip3


pip3 install -r requirements.txt


## TODO
* [ ] Fill in Creatin pipeline
* [ ] Fill in Train from local machine
* [ ] Include checkout experiments tab while waiting for experiments and after
* [ ] Notebook for Pipeline
* [ ] Notebook for Train and register models

### Extra taskts
Download repo, and install requirements then run files. This is to show that you can work from local computer also.  
* [ ] Script that get the dataset