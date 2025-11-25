import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from xgboost import XGBRegressor
import joblib
from oil_retail import logger
from oil_retail.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_df = pd.read_csv(self.config.train_data)
        test_df = pd.read_csv(self.config.test_data)

        target = "volume"

        X_train = train_df.drop(columns=[target])
        y_train = train_df[target]

        X_test = test_df.drop(columns=[target])
        y_test = test_df[target]

        model = XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            colsample_bytree=0.9,
            random_state=42
        )

        logger.info("Training model...")
        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        rmse = mean_squared_error(y_test, preds, squared=False)
        mape = mean_absolute_percentage_error(y_test, preds) * 100

        logger.info(f"RMSE: {rmse}")
        logger.info(f"MAPE: {mape}")

        joblib.dump(model, self.config.model_path)
        logger.info(f"Model saved at {self.config.model_path}")

        return rmse, mape
