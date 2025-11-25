from oil_retail import logger
from oil_retail.pipline.stage01_data_ingestion import DataIngestionTrainingPipeline
from oil_retail.pipline.stage02_data_val import DataValidationTrainingPipeline

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