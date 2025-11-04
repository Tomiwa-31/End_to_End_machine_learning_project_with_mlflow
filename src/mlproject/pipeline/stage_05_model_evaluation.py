from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger


STAGE_NAME="Model_Evaluation_Stage"

class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>{STAGE_NAME} has started>>>>")
        obj=ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>{STAGE_NAME} is completed")

    except Exception as e:
        logger.exception(e)
        raise e



