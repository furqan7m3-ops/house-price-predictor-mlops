from zenml import pipeline, step, Model
from steps.data_ingestion_step import ingest_data
from steps.handle_missing_values_step import handle_missing_values
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_handling_step import handle_outliers
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
    raw_data = ingest_data(file_path='D:\\Web Development\\Web Dev Python\\AI Based Web Projects\\House Price Prediction\\dataset\\archive.zip')
    cleaned_data = handle_missing_values(raw_data, strategy='drop', axis=0)
    cleaned_data = handle_missing_values(cleaned_data, strategy='mean')
    cleaned_data = handle_missing_values(cleaned_data, strategy='mode')
    
    transformed_data = handle_outliers(transformed_data)
    transformed_data = feature_engineering_step(cleaned_data)


if __name__ == "__main__":
    training_pipeline()