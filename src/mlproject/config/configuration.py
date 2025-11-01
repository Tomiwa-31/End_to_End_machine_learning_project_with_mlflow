from mlproject.constants import *
from mlproject.utils.common import read_yaml, create_directories
from mlproject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataTransformationConfig)


#creating a class configurationManager

class ConfigurationManager():
    def __init__(self,config_path=CONFIG_FILE_PATH,params_path=PARAMS_FILE_PATH,schema_path=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_path)
        self.params=read_yaml(params_path)
        self.schema=read_yaml(schema_path)

        create_directories([self.config.artifacts_root])

    def get_ingestion_configuration(self):
        self.data_ingestion=self.config.data_ingestion
        create_directories([self.data_ingestion.root_dir])

        #return an instance of the dataingestionclass

        data_ingestion_config= DataIngestionConfig(
            root_dir=Path(self.data_ingestion.root_dir),
            source_url=self.data_ingestion.source_url,
            local_data_file=Path(self.data_ingestion.local_data_file),
            unzip_dir=self.data_ingestion.unzip_dir

        )

        return data_ingestion_config
    
    def get_validation_data(self):
        config=self.config.data_validation
        schema=self.schema.columns
        data_validation=create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema


        )
    
    def get_data_transformation_config(self):
        config=self.config.data_transformation

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )