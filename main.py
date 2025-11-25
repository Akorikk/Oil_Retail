from oil_retail import logger
from oil_retail.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from oil_retail.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from oil_retail.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from oil_retail.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from oil_retail.pipeline.stage05_model_monitoring import ModelMonitoringPipeline


STAGE_NAME = "data ingestion"
try:
    logger.info(f"stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e    



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e

STAGE_name =  "Model trainer"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(e)
    raise e


if __name__ == "__main__":
    try:
        model_monitoring = ModelMonitoringPipeline()
        model_monitoring.main()

        logger.info(">>>>>>> Model Monitoring Stage Completed <<<<<<<<")
    except Exception as e:
        raise e
