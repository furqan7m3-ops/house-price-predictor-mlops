from zenml import step
from src.ingest_data import DataIngestorFactory
import pandas as pd
import os
@step
def ingest_data(file_path: str) -> pd.DataFrame:
    """
    Pipeline step for defining the data ingestion logic (.zip file ingestion)
    """
    file_extension = os.path.splitext(file_path)
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    return df