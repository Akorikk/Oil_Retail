from oil_retail.config.configuration import ConfigurationManager
from oil_retail.components.model_trainer import ModelTrainer
from oil_retail import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()

        trainer = ModelTrainer(model_trainer_config)
        trainer.train()
