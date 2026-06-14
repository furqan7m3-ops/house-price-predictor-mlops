from zenml import logger, step
from src.feature_engineering import FeatureEngineeringPipeline
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@step
def feature_engineering_step(df):
    feature_engineering_pipeline = FeatureEngineeringPipeline()
    features={
        'numerical': df.select_dtypes(include='number').columns.tolist(),
        'nominal': df.select_dtypes(include=['object', 'category']).columns.tolist(),
    }
    transformed_df  = feature_engineering_pipeline.transform(df, features['numerical'], features['nominal'])

    logger.info("Step 3. Feature Engineering...")
    logger.info('Transformed Data: ')
    logger.info(transformed_df)
    logger.info('-'*10)
    return transformed_df