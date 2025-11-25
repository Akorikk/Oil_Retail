# Oil_Retail

End-to-End Project Summary: Fuel Price Optimization System (Full MLOps Pipeline)

You have successfully built a complete, production-grade Machine Learning system that predicts fuel volume and recommends the best retail price for a petrol company.
This is not just ML — it's a full MLOps project like a real company would build.

✅ 1. Problem Solved

The business objective:

Optimize daily fuel price to maximize profit

Given:

Company price

Competitor prices

Cost

Historical volume

You built a model that predicts volume, then uses it to recommend the price that gives maximum profit.

✅ 2. What You Built (Full Pipeline)
✔ Data Ingestion

Downloads data automatically from GitHub.

Extracts the ZIP file.

Saves raw dataset in artifacts folder.

✔ Data Validation

Checks whether all required columns exist.

Writes validation status.

Ensures schema is correct before training.

✔ Data Transformation

Includes full feature engineering:

Price gap features

Lag features

Rolling averages

Removes NA

Drops date column (for XGBoost compatibility)

Outputs:

processed.csv

train.csv

test.csv

✔ Model Training (XGBoost)

Trains using parameters from params.yaml.

Evaluates using RMSE + MAPE.

Saves trained model as joblib:
artifacts/model_trainer/model.joblib

🔥 3. Price Optimization Engine

You built an engine that:

Tries many price values (e.g., 85 to 110)

Predicts volume for each price

Calculates profit
profit = (price - cost) * predicted_volume

Selects the best possible price

This is the core of the assignment — and you built it perfectly.

📊 4. MLflow Tracking

You integrated MLflow to:

Track experiments

Log parameters

Log RMSE & MAPE

Log trained model artifact

Create experiment dashboards

MLflow gives:

Reproducibility

Experiment comparison

Versioning of ML models

You can view it using:

mlflow ui

📈 5. Evidently AI Monitoring

You added data drift monitoring, including:

Data drift report (JSON)

Drift dashboard (HTML)

Uses reference (train) data vs current (test) data

This ensures your model stays healthy over time.

🐳 6. Dockerization (Production Packaging)

You created a Dockerfile that:

Uses Python 3.9 slim image

Installs dependencies

Runs the entire pipeline automatically

This makes your project:

✔ Portable
✔ Reproducible
✔ Deployable to AWS, GCP, Azure, Render, etc.

🔄 7. CI/CD (GitHub Actions)

You created a CI pipeline that:

Installs dependencies

Runs entire ML pipeline

Builds Docker image

Pushes Docker image to DockerHub

This gives real-world benefits:
✔ Automated build
✔ No manual errors
✔ Continuous integration
✔ Deployment-ready container

🌟 Tools Used & Why They Matter
Tool	Purpose	Benefit
Python (3.9)	Core language	ML ecosystem
Pandas / NumPy	Data manipulation	Fast processing
Scikit-learn	Splitting, metrics	Convenience tools
XGBoost	Regression model	High accuracy
MLflow	Experiment tracking	Versioning, comparison
Evidently AI	Drift monitoring	Model health monitoring
Joblib	Model saving	Efficient serialization
Docker	Containerization	Deploy anywhere
GitHub Actions	CI/CD automation	Professional workflow
YAML config system	Pipeline configuration	Clean maintainable code
Artifact-based pipeline	Store outputs cleanly	Real MLOps structure
🎯 What Makes This a True MLOps Project?
✔ Automated Data Ingestion
✔ Schema Validation
✔ Feature Engineering Pipeline
✔ Model Training + Evaluation
✔ Model Registry (MLflow)
✔ Monitoring (Evidently)
✔ Packaging (Docker)
✔ CI/CD (GitHub Actions)
✔ Code Modularized into Stages
✔ Config-driven architecture

This is EXACTLY how real ML pipelines are built in companies like Amazon, Uber, and Swiggy.

🏆 Final Outcome

You now have:

🔥 A COMPLETE Fuel Price Optimization Product:

Predicts future volume

Recommends best selling price

Tracks model performance

Detects data drift

Runs on Docker

Automated CI/CD pipeline

This project is highly impressive for an interview or portfolio.

⭐ If someone asks:
Why did you use MLflow?

Because MLflow allows:

Experiment tracking

Metric comparison

Model version control

Reproducibility

Why did you use Evidently AI?

Because Evidently provides:

Automated data drift detection

Monitoring dashboards

Production model health checks

These two tools make your project production-ready.

setup.py ==> I have use -e . in the end of requirements.txt to setup my local package you can see oil_retail is my local package because inside oil_retail we are having so many components now lets say i want to import something from oil_retail so we import like this from oil_retail.configuration import data_ingestion we can only import if it is set as a local package -e . it will look particular file called setup.py inside setup.py we have to give little details it is important to do if you wanna imort anything from oil_retail we can check using pip list if oil_retail is insatll as a local package or not 

Logging ==> Logging helps your project record what is happening while the code runs.It tells you the steps, warnings, and errors so you can debug easily.It creates a history of events (in a log file) so your ML pipeline becomes reliable and production-ready.

Utils ==> if you usinf the same function again and agian in your implementation lets say you want yo read yaml file so i need to read this yaml file in each and and every component like data ingetsion data validation model trainer etc so every time you need to write the same function again and again for reading this file insted of doing this we can create a one fucntion for yaml file and  we can keep inside the utils and whenever we need it we import it from utils iw will helps you to implement the project without repeting that function if you notice i have used ConfigBox and ensure_annotation in each and every function in utils what is the use of this ConfigBox lets you access dictionary keys like attributes, making your config files easier and cleaner to use. for example this is the code we have written from box import ConfigBox

config = ConfigBox({
    "project_name": "my_app",
    "version": 1.0
})

print(config.project_name)   # instead of config["project_name"]
print(config.version)  now we want to see version we write like this config["version"] so instead of writing this we can write like this config.version
if we are using configbox and next is ensure_annotations => It enforces that function arguments and return values follow Python type annotations at runtime. It checks if the types you annotated are actually correct when the function runs. Python does not check types for example def add(a: int, b: int) -> int:
    return a + b

add("10", 20) we can see that 10 is in string form 
it will give you unexpected result with no error Even though a should be an int, Python allows "10". With ensure_annotations Catches bugs early Stops wrong data types entering your functions and its will throw error the correxct way its makes large projects safer & more stable that why i have use ensure_annotations on top of all function written in utiles.common.py

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in oil_retail config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

so first we have to update config.yaml inside config.yaml fils we have to write some external variable  so firts variable would be data ingestion these are the variable we have to write 
artifacts_root: artifacts
data_ingestion:
  root_dir: artifacts/data_ingestion
  source_url: 
  local_data_file: artifacts/data_ingestion/data.zip
  unzip_dir: artifacts/data_ingestion
so i am creating folder name artifacts inside artifacts folder it will ingest my data by the given source url the we have to update our entity so entity is a return type of a function 
this is what we had to do in entity @dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
whatever you have seen in config.yaml i have defined here in entity and i have use frozen=True that means whatever variable i have defined here apart from thta if you want to define any other variable you cant because its already frozen 
so same workflow we gonna use for data validation data transformation etc for example you want to chanke the url you can change the source_url 

next is configuration this configuration will return all the configuration like root dir source url etc so inside constant i have put all the yaml file path and i am reading the file fron constant 

I used MLflow to track experiments, log metrics, store models, and maintain full reproducibility of the ML pipeline. It helps manage versions and monitor model performance during development.

I used Evidently AI to monitor data drift and model performance after training. It generates dashboards that show whether the model is still reliable in production.

Together, MLflow + Evidently AI provide a complete MLOps solution experiment tracking + continuous monitoring which makes the system production-ready and scalable.
use mlflow ui --backend-store-uri mlruns in command to see ui and for evidentaly ui runn the main.py it will runn the end to end pipeline and create artifact folder go to the folder then go to model_monitoring you can see two file data_drift_json and data_drift_dashboard.html run html to see ui 
 
