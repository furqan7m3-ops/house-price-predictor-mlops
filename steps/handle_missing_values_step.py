from matplotlib import axis
from zenml import step
from src.handle_missing_values import MissingValuesHandler, FillMissingValuesStrategy, DropMissingValuesStrategy
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@step
def handle_missing_values(df: pd.DataFrame, strategy: str = "mean", axis: int = 0)-> pd.DataFrame:
    """
    Pipeline method for missing values handling.
    Parameters:
    df: pd.DataFrame (Input Dataset)
    strategy: str (Strategy or method such as mean, median etc)
    axis: int (Axis along which to drop or fill missing values)
    Returns:
    pd.DataFrame (Cleaned Dataset)
    """
    valid_strategies = ["mean", "median", "mode", "constant"]
    missing_values_handler = None
    if strategy == "drop":
        missing_values_handler = MissingValuesHandler(DropMissingValuesStrategy(axis=axis))
        
    elif strategy in valid_strategies:
        missing_values_handler = MissingValuesHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value strategy. The valid strategies are {valid_strategies.join(",")}.")
    
    cleaned_df = missing_values_handler.handle(df)
    logger.info("Step 2. Handling Missing Values...")
    logger.info('Cleaned Data: ')
    logger.info('-'*10)
    return cleaned_df