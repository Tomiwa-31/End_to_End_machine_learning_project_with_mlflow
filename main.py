from mlproject import logger  # Import the configured logger instance
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainngPipeline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_04_model_training import ModelTrainingPipeline
from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME="data_ingestion_stage"

try:
    logger.info(f">>>>{STAGE_NAME} has started")
    data_ingestion=DataIngestionTrainngPipeline()
    data_ingestion.main()
    logger.info(f">>>{STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="data_validation_stage"

try:
    logger.info(f">>>>{STAGE_NAME} has started")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>{STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data_Transformation_Stage"

try:
    logger.info(f">>>>{STAGE_NAME} has started")
    data_ingestion=DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>{STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model_traning_stage"

try:
    logger.info(f">>>>{STAGE_NAME} has started")
    data_ingestion=ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>{STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model_Evaluation_Stage"

try:
    logger.info(f">>>>{STAGE_NAME} has started")
    data_ingestion=ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>{STAGE_NAME} is completed")

except Exception as e:
    logger.exception(e)
    raise e
