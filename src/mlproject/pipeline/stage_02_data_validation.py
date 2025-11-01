from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import DataValidation
from mlproject import logger 

STAGE_NAME="Data_validation_stage"



class DataValidationTrainingPipeline():
    def __init__(self):
        pass
    def main():
        try:
            config=ConfigurationManager()
            data_validation_config=config.get_validation_data()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()

        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>{STAGE_NAME} started")
        obj=DataValidationTrainingPipeline
        obj.main()
        logger.info(f">>>{STAGE_NAME} completed")

    except Exception as e:
        logger.exception(e) 
        raise e

