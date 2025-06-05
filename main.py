from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_tranformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'
try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=============x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation Stage"
try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_transformation = DataTransformationPipeline()
        data_transformation.initiate_data_transformation()
        logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=============x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training Stage"
try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_training = ModelTrainingPipeline()
        model_training.initiate_model_training()
        logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=============x")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation Stage"
try: 
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.initiate_model_evaluation()
        logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<\n\nx=============x")

except Exception as e:
        logger.exception(e)
        raise e
       