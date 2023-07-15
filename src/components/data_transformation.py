from src.logger import logging
from src.exceptions import CustomException
import pandas as pd
import sys

class DataTransformation:
    def __init__(self) -> None:
        pass
    
    def initiate_data_transformation(self,data_path,column)->tuple:
        try:
            df=pd.read_csv(data_path)
            data=df[[column]]
            train_data=data.iloc[0:70]
            test_data=data.iloc[70:]
            history=[x for x in train_data[column]]
            test_data=[x for x in test_data[column]]
            return (history,test_data)
        except Exception as e:
            logging.info("error occured during data transformation")
            raise CustomException(e,sys)