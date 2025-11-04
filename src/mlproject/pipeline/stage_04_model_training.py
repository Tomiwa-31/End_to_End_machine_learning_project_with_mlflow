from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger

STAGE_NAME="Model_training_stage"

class ModelTrainingPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>{STAGE_NAME} has started>>>")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>{STAGE_NAME} is completed")

    except Exception as e:
        logger.exception(e)
        raise e

