import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from oil_retail import logger
from oil_retail.entity.config_entity import ModelMonitoringConfig

class ModelMonitoring:
    def __init__(self, config: ModelMonitoringConfig):
        self.config = config

    def run_monitoring(self):
        logger.info("Loading reference and current data for drift analysis...")

        ref_df = pd.read_csv(self.config.reference_data)
        cur_df = pd.read_csv(self.config.current_data)

        # Generate drift report (includes visual dashboard automatically)
        drift_report = Report(metrics=[DataDriftPreset()])
        drift_report.run(reference_data=ref_df, current_data=cur_df)
        
        # Save JSON
        drift_report.save_json(self.config.drift_report)

        # Save HTML
        drift_report.save_html(self.config.drift_dashboard)

        logger.info(f"Drift report saved at {self.config.drift_report}")
        logger.info(f"Drift dashboard saved at {self.config.drift_dashboard}")
