from oil_retail.constants import *
from oil_retail.utils.common import read_yaml, create_directories
from oil_retail.entity.config_entity import (DataIngestionConfig, 
                                             DataValidationConfig,
                                             DataTransformationConfig,
                                             ModelTrainerConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            processed_data=config.processed_data,
            train_data=config.train_data,
            test_data=config.test_data
        )

        return data_transformation_config
    

    """def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.model_trainer  

        create_directories([config.root_dir])


        return ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            model_path=config.model_path,
            params=params    
            )"""
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.model_trainer
        mlflow_cfg = self.params.mlflow

        create_directories([config.root_dir])

        return ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data=config.train_data,
            test_data=config.test_data,
            model_path=config.model_path,
            n_estimators=params.n_estimators,
            learning_rate=params.learning_rate,
            max_depth=params.max_depth,
            colsample_bytree=params.colsample_bytree,
            random_state=params.random_state,
            mlflow_tracking_uri=mlflow_cfg.tracking_uri,
            mlflow_experiment_name=mlflow_cfg.experiment_name
        )


