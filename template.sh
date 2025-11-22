# To run this sh template.sh

project_name="oil_retail"

# Creating Directories
mkdir -p $project_name/components
mkdir -p $project_name/configuration
mkdir -p $project_name/constants
mkdir -p $project_name/entity
mkdir -p $project_name/exception
mkdir -p $project_name/logger
mkdir -p $project_name/pipline
mkdir -p $project_name/utils
mkdir -p config

# Creating Files
touch $project_name/__init__.py
touch $project_name/components/__init__.py
touch $project_name/components/data_ingestion.py
touch $project_name/components/data_validation.py
touch $project_name/components/data_transformation.py
touch $project_name/components/model_trainer.py
touch $project_name/components/model_evaluation.py
touch $project_name/components/model_pusher.py

touch $project_name/configuration/__init__.py
touch $project_name/constants/__init__.py

touch $project_name/entity/__init__.py
touch $project_name/entity/config_entity.py
touch $project_name/entity/artifact_entity.py

touch $project_name/exception/__init__.py
touch $project_name/logger/__init__.py

touch $project_name/pipline/__init__.py
touch $project_name/pipline/training_pipeline.py
touch $project_name/pipline/prediction_pipeline.py

touch $project_name/utils/__init__.py
touch $project_name/utils/main_utils.py

touch app.py
touch requirements.txt
touch Dockerfile
touch .dockerignore
touch demo.py
touch setup.py
touch config/model.yaml
touch config/schema.yaml