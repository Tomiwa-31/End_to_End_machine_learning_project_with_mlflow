from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger

STAGE_NAME= "Data_Transformation_stage"

class DataTransformationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f">>>>{STAGE_NAME} has started")
        obj= DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>{STAGE_NAME} is completed")
    except Exception as e:
        logger.exception(e)
        raise e


