import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.logger import logging
from src.exceptions import CustomException

from sklearn.model_selection import train_test_split
from src.util import train_test_split_data
from src.components.data_trainer import ModelTrainer

from src.components.data_transformation import DataTransformation, DataTransformationConfig


# class DataIngestionConfig:
#     def __init__(self, train, test, raw):
#         self.train_data_path = os.path.join('artifacts', 'train.csv')
#         self.test_data_path = os.path.join('artifacts', 'test.csv')
#         self.raw_data_path = os.path.join("artifacts", 'raw.csv')

######## or ########
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join("artifacts", 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting to read the data")
        try:
           df = pd.read_csv("notebook/data/stud.csv")
           logging.info("Read the data as csv")
           

           # if exists then override it
           os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
           
           df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

           logging.info("splitting the data")
           train_data, test_data = train_test_split_data(df, 0.2)

           train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
           test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

           logging.info("Data Ingestion and division completed")

           return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)


        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()  

    data_transformation = DataTransformation()      
    train_arr, test_arr = data.transformation.initiate_data_transformation(train_path, test_path)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))