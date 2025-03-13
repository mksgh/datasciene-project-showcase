from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Trainer Stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        """start model training"""
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
