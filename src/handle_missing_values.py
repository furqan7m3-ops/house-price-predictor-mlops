from abc import ABC, abstractmethod
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class HandleMissingValuesStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame)-> pd.DataFrame:
        pass

class DropMissingValuesStrategy(HandleMissingValuesStrategy):
    def __init__(self, axis: int = 0, thresh: int = None):
        self.axis = axis
        self.thresh = thresh
    
    def handle(self, df: pd.DataFrame)->pd.DataFrame:
        logging.info(f"Drop missing values with axis= {self.axis} and thresh= {self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logging.info("Missing Values dropped successfully")
        return df_cleaned

class FillMissingValuesStrategy(HandleMissingValuesStrategy):
    def __init__(self, method: str = 'mean', fill_value=None):
        self.method = method
        self.fill_value = fill_value
    
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Filling missing values using method={self.method}")
        cleaned_df = df.copy()
        if self.method == 'mean':
            numerical_cols = cleaned_df.select_dtypes(include='number').columns
            cleaned_df[numerical_cols] = cleaned_df[numerical_cols].fillna(cleaned_df[numerical_cols].mean())
        elif self.method == 'median':
            numerical_cols = cleaned_df.select_dtypes(include='number').columns
            cleaned_df[numerical_cols] = cleaned_df[numerical_cols].fillna(cleaned_df[numerical_cols].median())
        elif self.method == 'mode':
            categorical_cols = cleaned_df.select_dtypes(include='object')
            cleaned_df[categorical_cols] = cleaned_df[categorical_cols].fillna(cleaned_df[categorical_cols].mode())
        elif self.method == 'constant':
            if self.fill_value:
                cleaned_df = cleaned_df.fillna(fill_value=self.fill_value)
        else:
            logging.info("Invalid Value for method valid valuese are: mean, median, mode and constant")
            raise ValueError("Invalid Value for method valid valuese are: mean, median, mode and constant")

class MissingValuesHandler:
    def __init__(self, strategy: HandleMissingValuesStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: HandleMissingValuesStrategy):
        self.strategy = strategy
    
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        self.strategy.handle(df)
