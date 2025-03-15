import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.dsproject.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,data):
        
        config = ConfigurationManager()
        model_path = config.get_model_prediction_config().model_path
        model = joblib.load(model_path)
        prediction=model.predict(data)

        return prediction