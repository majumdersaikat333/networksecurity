from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerComfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys
    
if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        data_ingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestionconfig)
        logging.info("Initiate the dataingestion")

        data_ingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiaion completed")
        print(data_ingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_ingestionartifact, data_validation_config)
        logging.info("initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

        logging.info("Model Training sstared")
        model_trainer_config = ModelTrainerComfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()


        

    except Exception as e:
        raise NetworkSecurityException(e,sys)