# End_to_End_machine_learning_project_wine_quality_prediction_with_mlflow





## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port

```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Tomiwa-31/End_to_End_machine_learning_project_with_mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=Tomiwa-31
MLFLOW_TRACKING_PASSWORD= c215d3db8ce16bbf4e203e713fce988d8a289887
python script.py


JUPYTER NOTEBOOK/Testing/DEVELOPMENT

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Tomiwa-31/End_to_End_machine_learning_project_with_mlflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Tomiwa-31"
os.environ["MLFLOW_TRACKING_PASSWORD"]="c215d3db8ce16bbf4e203e713fce988d8a289887"


Run this to export as env variables:
TERMINAL=PRODUCTION EXECUTION

```bash

set MLFLOW_TRACKING_URI=ttps://dagshub.com/Tomiwa-31/End_to_End_machine_learning_project_with_mlflow.mlflow

set MLFLOW_TRACKING_USERNAME=Tomiwa-31

set MLFLOW_TRACKING_PASSWORD=c215d3db8ce16bbf4e203e713fce988d8a289887

 76e7177fa1749d418308c043cb888bb52af04c50
