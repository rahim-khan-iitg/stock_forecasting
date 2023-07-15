from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import warnings 
warnings.filterwarnings('ignore')
def start_training(key,col):
    obj=DataIngestion()
    data_path=obj.initiate_data_ingestion(key)
    # print(data_path)
    obj2=DataTransformation()
    history,test_data=obj2.initiate_data_transformation(data_path,col)
    # print("data transformation complete")
    # print("model training started")
    # obj3=ModelTrainer()
    # obj3.initiate_model_training(history,test_data)
    # print("complete")
    return (history,test_data)