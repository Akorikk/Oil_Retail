from oil_retail.config.configuration import ConfigurationManager
from oil_retail.components.data_transformation import DataTransformation
from oil_retail import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r")as f:
                status = f.read().split(" ")[-1]

            if status =="True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(data_transformation_config)
        
                    df = data_transformation.transform()
                    data_transformation.split_data()

            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
             print(e)    
                
    