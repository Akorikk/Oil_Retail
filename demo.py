from oil_retail import logger
from oil_retail.pipline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "data ingestion"
try:
    logger.info(f"stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e    