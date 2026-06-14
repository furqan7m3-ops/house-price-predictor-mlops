from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
class Feature_engineeringTemplate(ABC):
    def transform(self, df: pd.DataFrame, numerical_features: list[str], nominal_features: list[str],  ordinal_features: list[str]= None) -> pd.DataFrame:
        transformed_df =self.apply_feature_transformation(df, numerical_features)
        scaled_df = self.scale_numerical_features(transformed_df, numerical_features)
        if ordinal_features is not None:
            scaled_df = self.encode_ordinal_features(scaled_df, ordinal_features)
        scaled_df = self.encode_nominal_features(scaled_df, nominal_features)
        return scaled_df
    
    @abstractmethod
    def apply_feature_transformation(self, df: pd.DataFrame, numerical_features: list[str]):
        pass
    @abstractmethod
    def scale_numerical_features(self, df: pd.DataFrame, numerical_features: list[str]):
        pass
    @abstractmethod
    def encode_ordinal_features(self, df: pd.DataFrame, ordinal_features: list[str]):
        pass
    @abstractmethod
    def encode_nominal_features(self, df: pd.DataFrame, nominal_features: list[str]):
        pass

class FeatureScalingStrategy(ABC):
    @abstractmethod
    def scale(self, df: pd.DataFrame, numerical_features: list[str]) -> pd.DataFrame:
        pass

class StandardFeatureScaler(FeatureScalingStrategy):
    def scale(self, df: pd.DataFrame, numerical_features: list[str]) -> pd.DataFrame:
        scaled_df = df.copy()
        scaled_df[numerical_features] = (scaled_df[numerical_features] - scaled_df[numerical_features].mean(axis=0)) / scaled_df[numerical_features].std(axis=0)
        return scaled_df

class MinMaxFeatureScaler(FeatureScalingStrategy):
    def scale(self, df: pd.DataFrame, numerical_features: list[str]) -> pd.DataFrame:
        scaled_df = df.copy()
        scaled_df[numerical_features] = (scaled_df[numerical_features] - scaled_df[numerical_features].min(axis=0)) / (scaled_df[numerical_features].max(axis=0) - scaled_df[numerical_features].min(axis=0))
        return scaled_df

class FeatureScaler:
    def __init__(self, strategy: FeatureScalingStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: FeatureScalingStrategy):
        self.strategy = strategy
    
    def scale_features(self, df: pd.DataFrame, numerical_features: list[str]) -> pd.DataFrame:
        scaled_df = self.strategy.scale(df, numerical_features)
        return scaled_df


class FeatureTransformationStrategy(ABC):
    @abstractmethod
    def transform_features(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        pass
    

class LogTransform(FeatureTransformationStrategy):
    def transform_features(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        transformed_df = df.copy()
        transformed_df[features] = np.log1p(transformed_df[features])
        return transformed_df
    
class FeatureTransformer:
    def __init__(self, strategy: FeatureTransformationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: FeatureTransformationStrategy):
        self.strategy = strategy
    
    def transform_features(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        return self.strategy.transform_features(df, features)


class FeatureEncodingStrategy(ABC):
    @abstractmethod
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        pass

class OrdinalEncodingStrategy(FeatureEncodingStrategy):
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        ordinal_encoder = OrdinalEncoder()
        df_encoded = df.copy()
        encoded_features = ordinal_encoder.fit_transform(df[features])
        df_encoded[features] = encoded_features
        return df_encoded

class OneHotEncodingStrategy(FeatureEncodingStrategy):
    def encode(self, df: pd.DataFrame, features: list[str]) -> pd.DataFrame:
        transformed_df = df.copy()
        onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        encoded_features = onehot_encoder.fit_transform(df[features])
        feature_names = onehot_encoder.get_feature_names_out(features)
        transformed_df[feature_names] = encoded_features
        transformed_df.drop(columns=features, inplace=True)
        return transformed_df

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
        self.encoder = FeatureEncoder(strategy=OneHotEncodingStrategy())

    def apply_feature_transformation(self, df: pd.DataFrame, numerical_features: list[str]):
        return self.transformer.transform_features(df, numerical_features)
    
    def scale_numerical_features(self, df: pd.DataFrame, numerical_features: list[str]):
        return self.scaler.scale_features(df, numerical_features)

    def encode_nominal_features(self, df: pd.DataFrame, nominal_features: list[str]):
        self.encoder.set_strategy(OneHotEncodingStrategy())
        return self.encoder.encode_features(df, nominal_features)
    
    def encode_ordinal_features(self, df: pd.DataFrame, ordinal_features: list[str]):
        self.encoder.set_strategy(OrdinalEncodingStrategy())
        return self.encoder.encode_features(df, ordinal_features)