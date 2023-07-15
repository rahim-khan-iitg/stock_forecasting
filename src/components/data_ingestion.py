import os
import sys
from src.logger import logging
from src.exceptions import CustomException
import requests
import pandas as pd

from dataclasses import dataclass
 


@dataclass
class DataIngestionConfig:
    data_path=os.path.join("artifacts","stcoks.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self,key):
        try:
            data_url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={key}&output_size=compact&apikey=GQOYD08LEGBA4H3G"
            os.makedirs(os.path.dirname(self.ingestion_config.data_path),exist_ok=True)
            logging.info("data ingestion initiated")
            logging.info("fetching data from api")
            response=requests.get(data_url)
            json_data=response.json()
            logging.info("reading data in DataFrame")
            df=pd.DataFrame(json_data["Time Series (Daily)"])
            df=df.T
            df.columns=['open', 'high', 'low', 'close', 'adjusted_close','volume', 'dividend_amount', 'split_coefficient']
            df.open=df.open.astype('float')
            df.high=df.high.astype('float')
            df.low=df.low.astype('float')
            df.close=df.close.astype('float')
            df.adjusted_close=df.adjusted_close.astype('float')
            df.volume=df.volume.astype('float')
            df.split_coefficient=df.split_coefficient.astype('float')
            df=df.iloc[::-1]
            logging.info("saving the csv file")

            df.to_csv(self.ingestion_config.data_path,index=True,header=True)
            logging.info("Data Ingestion complete")
            return self.ingestion_config.data_path
        
        except Exception as e:
            logging.info("error occured during data ingestion")
            raise CustomException(e,sys)
