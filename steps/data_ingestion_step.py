from zenml import step
from src.ingest_data import DataIngestorFactory
import pandas as pd
import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@step
def ingest_data(file_path: str) -> pd.DataFrame:
    """
    Pipeline step for defining the data ingestion logic (.zip file ingestion)
    """
    file_extension = os.path.splitext(file_path)[-1]
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    logger.info("Step 1. Data Ingestion...")
    logger.info('Raw Data: ')
    logger.info(df)
    logger.info('-'*10)

    return df