from zenml import pipeline, step, Model
from steps.data_ingestion_step import ingest_data
from steps.hande_missing_values_step import handle_missing_values
@pipeline(
    model=Model(
        #This name uniquely identifies this model
        name="house_price_predictor"
    )
)
def training_pipeline():
    """
    Defines and end to end pipeline for training house price predictor model
    """
    raw_data = ingest_data(file_path='../dataset/archive.zip')
    cleaned_data = handle_missing_values(raw_data, strategy='mean')
    pass