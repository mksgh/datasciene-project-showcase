import os
import zipfile
import urllib.request as request
from src.dsproject import logger
from src.dsproject.entity.config_entity import DataIngestionConfig


## component-Data Ingestion

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    # Downloading the zip file
    def download_file(self):
        """Download the zip file from the source
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"'{self.config.local_data_file}' file already exists")

    def extract_zip_file(self):
        """Extracts the zip file into the data directory

        zip_file_path: str
        Returns: None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)