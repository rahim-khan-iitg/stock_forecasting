from src.logger import logging
from src.exceptions import CustomException
from src.pipelines.training_pipeline import start_training
from statsmodels.tsa.arima.model import ARIMA
import sys
class predict:
    def __init__(self,key,col) -> None:
        self.key=key
        self.col=col
    def make_prediction(self):
        try:
            logging.info("making prediction for new data point")
            history,test=start_training(self.key,self.col)
            pred=list()
            for i in range(len(test)):
                m=ARIMA(history,order=(1,1,1))
                res=m.fit()
                prediction=res.forecast()
                pred.append(prediction[0])
                history.append(test[i])
            m=ARIMA(history,order=(1,1,1))
            res=m.fit()
            next=res.forecast()
            return (test,pred,next)
        except Exception as e:
            logging.info("error occured during the prediction")
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=predict("IBM","close")
    test,pred,next=obj.make_prediction()
    print("test ",test)
    print("pred ",pred)
    print("next ",next)