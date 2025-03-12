import os
import pandas as pd
from src.dsproject import logger
from sklearn.model_selection import train_test_split
from src.dsproject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        """Split data into train and test and saving them to csv file"""

        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets.
        train, test = train_test_split(data, test_size=0.20)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted the data into training and test sets")
        logger.info(f"Shape of train data {train.shape}")
        logger.info(f"Shape of train data {train.shape}")

        print(f"Shape of train data {train.shape}")
        print(f"Shape of train data {train.shape}")
