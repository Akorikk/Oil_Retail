import pandas as pd
import mlflow
import mlflow.sklearn
from joblib import dump
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from xgboost import XGBRegressor
from oil_retail import logger
from oil_retail.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Load data
        train_df = pd.read_csv(self.config.train_data)
        test_df = pd.read_csv(self.config.test_data)

        # Split features & target
        X_train = train_df.drop(columns=["volume"])
        y_train = train_df["volume"]

        X_test = test_df.drop(columns=["volume"])
        y_test = test_df["volume"]

        # Initialize model
        model = XGBRegressor(
            n_estimators=self.config.n_estimators,
            learning_rate=self.config.learning_rate,
            max_depth=self.config.max_depth,
            colsample_bytree=self.config.colsample_bytree,
            random_state=self.config.random_state
        )

        logger.info("Training model...")

        # ========= MLflow Tracking ===========
        mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
        mlflow.set_experiment(self.config.mlflow_experiment_name)

        with mlflow.start_run():

            # Log hyperparameters
            mlflow.log_params({
                "n_estimators": self.config.n_estimators,
                "learning_rate": self.config.learning_rate,
                "max_depth": self.config.max_depth,
                "colsample_bytree": self.config.colsample_bytree,
                "random_state": self.config.random_state
            })

            # Train model
            model.fit(X_train, y_train)

            # Predictions
            y_pred = model.predict(X_test)

            # Metrics
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            mape = mean_absolute_percentage_error(y_test, y_pred)

            logger.info(f"RMSE: {rmse}")
            logger.info(f"MAPE: {mape}")

            # Log metrics
            mlflow.log_metrics({
                "rmse": rmse,
                "mape": mape
            })

            # Log model
            mlflow.sklearn.log_model(model, "model")

            # Save model locally
            dump(model, self.config.model_path)
            logger.info(f"Model saved at {self.config.model_path}")

        return model



"""import pandas as pd
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

        return rmse, mape """
