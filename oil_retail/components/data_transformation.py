import os
import pandas as pd
from oil_retail import logger
from oil_retail.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform(self):
        df = pd.read_csv(self.config.data_path)

        # Convert date
        df['date'] = pd.to_datetime(df['date'])

        # Price gaps
        df['gap_comp1'] = df['price'] - df['comp1_price']
        df['gap_comp2'] = df['price'] - df['comp2_price']
        df['gap_comp3'] = df['price'] - df['comp3_price']

        # Lag features
        df['price_lag_1'] = df['price'].shift(1)
        df['volume_lag_1'] = df['volume'].shift(1)

        # Moving averages
        df['volume_ma_7'] = df['volume'].rolling(window=7).mean()
        df['volume_ma_30'] = df['volume'].rolling(window=30).mean()

        # Drop missing
        df = df.dropna()

        # Save processed dataset
        df.to_csv(self.config.processed_data, index=False)
        logger.info(f"Processed data saved at {self.config.processed_data}")

        return df

    def split_data(self):
        df = pd.read_csv(self.config.processed_data)

        train_size = int(len(df) * 0.8)

        train = df.iloc[:train_size]
        test = df.iloc[train_size:]

        train.to_csv(self.config.train_data, index=False)
        test.to_csv(self.config.test_data, index=False)

        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")
