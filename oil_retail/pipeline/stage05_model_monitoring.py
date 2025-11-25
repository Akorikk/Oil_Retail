from oil_retail.config.configuration import ConfigurationManager
from oil_retail.components.model_monitoring import ModelMonitoring
from oil_retail import logger

STAGE_NAME = "Model Monitoring Stage"

class ModelMonitoringPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        monitor_config = config.get_model_monitoring_config()
        monitoring = ModelMonitoring(monitor_config)
        monitoring.run_monitoring()
