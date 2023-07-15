import pickle
import os
import sys
from src.logger import logging
from src.exceptions import CustomException
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import numpy as np  

def save_object(file_path:str,obj):
    try:
        logging.info("saving object")
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        pickle.dump(obj,open(file_path,'wb'))
        logging.info("object saved successfully")
    except Exception as e:
        logging.info("error occured while saving the model")
        raise CustomException(e,sys)


def train_arima_model(X, y, arima_order):
    # logging.info(f"training the model for the order {arima_order}")
    history = [x for x in X]
    predictions = list()
    for t in range(len(y)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(y[t])
    rmse = np.sqrt(mean_squared_error(y, predictions))
    return rmse
def evaluate_models(train,test,p_values,d_values,q_values):
    logging.info("model evaluation started")
    best_score,best_cfg=float("inf"),None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order=(p,d,q)
                try:
                    rmse=train_arima_model(train,test,order)
                    if rmse<best_score:
                        best_score,best_cfg=rmse,order
                    logging.info(f"ARIMA{order} RMSE={rmse}")
                except:
                    continue
    logging.info(f"best ARIMA{best_cfg} RMSE={best_score}")
    logging.info("model evaluation completed")
    return best_cfg

def load_model():
    model=pickle.load(open(os.path.join("artifacts",'model.pkl'),'rb'))
    return model