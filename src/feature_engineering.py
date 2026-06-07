from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
class Feature_engineeringTemplate(ABC):
    def transform(self, df: pd.DataFrame, ordinal_features: list, nominal_features: list) -> pd.DataFrame:
        numerical_features = df.select_dtypes(include='number').columns
        self.apply_feature_transformation(df, numerical_features)
        self.scale_numerical_features(df, numerical_features)
        self.encode_ordinal_features(df, ordinal_features)
        self.encode_nominal_features(df, nominal_features)
        return df
    
    @abstractmethod
    def apply_feature_transformation(self, df: pd.DataFrame, numerical_features: list):
        pass
    @abstractmethod
    def scale_numerical_features(self, df: pd.DataFrame, numerical_features: list):
        pass
    @abstractmethod
    def encode_ordinal_features(self, df: pd.DataFrame, ordinal_features: list):
        pass
    @abstractmethod
    def encode_nominal_features(self, df: pd.DataFrame, nominal_features: list):
        pass

class FeatureScalingStrategy(ABC):
    @abstractmethod
    def scale(df: pd.DataFrame)->pd.DataFrame:
        pass

class StandardFeatureScaler(FeatureScalingStrategy):
    def scale(df: pd.DataFrame) -> pd.DataFrame:
        scaled_df = df.copy()
        scaled_df = scaled_df - scaled_df.mean(axis=0) / scaled_df.std(axis=0)
        return scaled_df

class MinMaxFeatureScaler(FeatureScalingStrategy):
    def scale(df: pd.DataFrame) -> pd.DataFrame:
        scaled_df = df.copy()
        scaled_df = (scaled_df - scaled_df.min(axis=0)) / (scaled_df.max(axis=0) - scaled_df.min(axis=0))
        return scaled_df

class FeatureScaler:
    def __init__(self, strategy: FeatureScalingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: FeatureScalingStrategy):
        self.strategy = strategy
    
    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        scaled_df = self.strategy.scale(df)
        return scaled_df


class FeatureTransformationStrategy(ABC):
    @abstractmethod
    def transform_features(df: pd.DataFrame) -> pd.DataFrame:
        pass
    

class LogTransform(FeatureTransformationStrategy):
    def transform_features(df: pd.DataFrame) -> pd.DataFrame:
        transformed_df = np.log1p(df)
        return transformed_df
    
class FeatureTransformer:
    def __init__(self, strategy: FeatureTransformationStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy:FeatureTransformationStrategy):
        self.strategy = strategy
    
    def transform_features(self, df: pd.DataFrame) -> pd.DataFrame:
        self.strategy.transform_features(df)


class FeatureEncodingStrategy(ABC):
    @abstractmethod
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        pass

class OrdinalEncodingStrategy(FeatureEncodingStrategy):
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        ordinal_encoder = OrdinalEncoder()
        df[features] = ordinal_encoder.fit_transform(df[features])
        return df

class OneHotEncodingStrategy(FeatureEncodingStrategy):
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        onehot_encoder = OneHotEncoder(sparse=False)
        encoded_features = onehot_encoder.fit_transform(df[features])
        feature_names = onehot_encoder.get_feature_names_out(features)
        df[feature_names] = encoded_features
        return df

class FeatureEncoder:
    def __init__(self, strategy: FeatureEncodingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: FeatureEncodingStrategy):
        self.strategy = strategy
    
    def encode_features(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        return self.strategy.encode(df, features)

class FeatureEngineeringPipeline(Feature_engineeringTemplate):
    def __init__(self):
        self.transformer = FeatureTransformer(LogTransform())
        self.scaler = FeatureScaler(StandardFeatureScaler())
        self.encoder = FeatureEncoder(strategy=None)

    def apply_feature_transformation(self, df: pd.DataFrame, numerical_features: list):
        self.transformer.transform_features(df[numerical_features])
    
    def scale_numerical_features(self, df: pd.DataFrame, numerical_features: list):
        scaled_features = self.scaler.scale_features(df[numerical_features])
        df[numerical_features] = scaled_features

    def encode_nominal_features(self, df: pd.DataFrame, nominal_features: list):
        self.encoder.encode_features(df, nominal_features)
    
    def encode_ordinal_features(self, df: pd.DataFrame, ordinal_features: list):
        self.encoder.encode_features(df, ordinal_features)
    