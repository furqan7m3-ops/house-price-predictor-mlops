from zenml import step
from src.outlier_detection import OutliersHandler, ZScoreStrategy, OutliersImputationHandlerStrategy
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@step
def handle_outliers(df: pd.DataFrame):
    features = df.select_dtypes(include='number').columns.tolist()
    outlier_handler = OutliersHandler(OutliersImputationHandlerStrategy( ZScoreStrategy(), fill_strategy='mean'))
    df_cleaned = outlier_handler.handle_outliers(df, features)

    logger.info("Step 4. Outlier Handling...")
    logger.info('Cleaned Data: ')
    logger.info(df_cleaned)
    logger.info('-'*10)
    return df_cleaned