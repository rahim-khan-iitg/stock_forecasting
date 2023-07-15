from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from src.utils import save_object,evaluate_models
import os
import sys
from src.exceptions import CustomException
from src.logger import logging


from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self) -> None:
        self.trainer_config=ModelTrainerConfig()
    
    def initiate_model_training(self,train_data,test_data):
        try:
            logging.info("model training initiated")    
            p_values=range(3)
            d_values=range(3)
            q_values=range(3)
            logging.info("evaluating models")
            best_order=evaluate_models(train_data,test_data,p_values,d_values,q_values)
            model=ARIMA(train_data,order=best_order)
            res=model.fit()
            logging.info("best model fitted")
            logging.info("saving the best model")
            save_object(self.trainer_config.trained_model_file_path,res)
        except Exception as e:
            logging.info("error occured during the model training")
            raise CustomException(e,sys)