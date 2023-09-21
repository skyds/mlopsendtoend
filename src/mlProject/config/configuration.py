from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_fileloc = CONFIG_FILE_LOC,
        params_fileloc = PARAMS_FILE_LOC,
        schema_fileloc = SCHEMA_FILE_LOC):

        self.config = read_yaml(config_fileloc)
        self.params = read_yaml(params_fileloc)
        self.schema = read_yaml(schema_fileloc)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        ) 

        return data_ingestion_config