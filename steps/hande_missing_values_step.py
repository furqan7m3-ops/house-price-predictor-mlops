from zenml import step
from src.handle_missing_values import MissingValuesHandler, FillMissingValuesStrategy, DropMissingValuesStrategy
import pandas as pd
@step
def handle_missing_values(df: pd.DataFrame, strategy: str = "mean")-> pd.DataFrame:
    """
    Pipeline method for missing values handling.
    Parameters:
    df: pd.DataFrame (Input Dataset)
    strategy: str (Strategy or method such as mean, median etc)
    Returns:
    pd.DataFrame (Cleaned Dataset)
    """
    valid_strategies = ["mean", "median", "mode", "constant"]
    missing_values_handler = None
    if strategy == "drop":
        missing_values_handler = MissingValuesHandler(DropMissingValuesStrategy(axis=0))
    elif strategy in valid_strategies:
        missing_values_handler = MissingValuesHandler(FillMissingValuesStrategy(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value strategy. The valid strategies are {valid_strategies.join(",")}.")
    
    cleaned_df = missing_values_handler.handle(df)
    return cleaned_df