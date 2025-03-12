from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.data_transformation import DataTransformation

from pathlib import Path

STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            config=ConfigurationManager()
            status_path = config.get_data_validation_config().STATUS_FILE

            with open(Path(status_path),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
            
        except Exception as e:
            print(e)