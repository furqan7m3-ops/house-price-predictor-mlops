from abc import ABC, abstractmethod
import pandas as pd


class OutlierDetectionStrategy(ABC):

    @abstractmethod
    def detect_outliers(
        self,
        df: pd.DataFrame,
        features: list[str]
    ) -> pd.DataFrame:
        pass


class ZScoreStrategy(OutlierDetectionStrategy):

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold

    def detect_outliers(
        self,
        df: pd.DataFrame,
        features: list[str]
    ) -> pd.DataFrame:


        z_scores = (
            df[features] -
            df[features].mean()
        ) / df[features].std()

        mask = z_scores.abs() > self.threshold
        return mask
    
class IQRStrategy(OutlierDetectionStrategy):

    def __init__(self, multiplier: float = 1.5):
        self.multiplier = multiplier

    def detect_outliers(
        self,
        df: pd.DataFrame,
        features: list[str]
    ) -> pd.DataFrame:

        Q1 = df[features].quantile(0.25)
        Q3 = df[features].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - self.multiplier * IQR
        upper_bound = Q3 + self.multiplier * IQR

        mask = (df[features] < lower_bound) | (df[features] > upper_bound)
        return mask


class OutlierHandlingStrategy(ABC):
    @abstractmethod
    def handle_outliers(self, df: pd.DataFrame, features: list[str])->pd.DataFrame:
        pass

class OutliersImputationHandlerStrategy(OutlierHandlingStrategy):
    def __init__(self, detection_strategy: OutlierDetectionStrategy, fill_strategy: str = 'mean'):
        self.fill_strategy = fill_strategy
        self.detection_strategy = detection_strategy
    
    def set_fill_strategy(self, fill_strategy: str):
        self.fill_strategy = fill_strategy

    def handle_outliers(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        df_cleaned = df.copy()
        outliers_mask = self.detection_strategy.detect_outliers(df, features)
        temp_df = df_cleaned[features].mask(outliers_mask)
        if self.fill_strategy == 'mean':
            fill_val = temp_df.mean()
        elif self.fill_strategy == 'median':
            fill_val = temp_df.median()
        else:
            raise ValueError('Invalid fill strategy valid values for impute strategy are: mean, median')
        df_cleaned[features] = df_cleaned[features].mask(outliers_mask, fill_val, axis=1)
        return df_cleaned

class OutliersHandler:
    def __init__(self, outlier_handler_strategy: OutlierHandlingStrategy):
        self.outlier_handler_strategy = outlier_handler_strategy
    def handle_outliers(self, df: pd.DataFrame, features: list[str])-> pd.DataFrame:
        df_cleaned = self.outlier_handler_strategy.handle_outliers(df, features)
        return df_cleaned