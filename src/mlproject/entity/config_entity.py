from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)   #contains all the vital information that would serve as atribute when creating the data_ingestion class
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:str

@dataclass(frozen=True)
class DataValidationConfig():
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

@dataclass(frozen=True)
class DataTransformationConfig():
    root_dir:Path
    data_path:Path