from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Performs Bivariate Analysis on the specified features of the DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature1 (str): The name of the first feature/column to analyze.
        feature2 (str): The name of the second feature/column to analyze.
        """
        pass

class NumericalvsNumericalBivariateStrategy(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Performs Bivariate analysis on specified numerical features of DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature1 (str): The name of the first feature/column to analyze.
        feature2 (str): The name of the second feature/column to analyze.
        """
        plt.figure(figsize=(10, 5))
        plt.title(f"Scatterplot showing the relationship between {feature1} and {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        sns.scatterplot(data=df, x=feature1, y=feature2)
        plt.show()

class NumericalvsCategoricalStrategy(BivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, numerical_feature: str, categorical_feature: str):
        """
        Performs Bivariate analysis on one numerical and one categorical feature
        of DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        numerical_feature (str): The name of the first feature/column to analyze.
        categorical_feature (str): The name of the second feature/column to analyze.
        Returns:
        None
        """
        plt.figure(figsize=(10, 5))
        plt.title("Boxplot showing the relation ship between one numerical and one categorical feature")
        plt.xlabel(categorical_feature)
        plt.ylabel(numerical_feature)
        sns.boxplot(data=df, x=categorical_feature, y=numerical_feature)
        plt.show()


class CategoricalvsCategoricalStrategy(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Performs Bivariate analysis on specified categorical features of DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature1 (str): The name of the first feature/column to analyze.
        feature2 (str): The name of the second feature/column to analyze.
        """
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        axs[0].set_title("Countplot showing the relationship between two categorical features")
        axs[0].set_xlabel(feature1)
        axs[0].set_ylabel(feature2)
        sns.countplot(data=df, x=feature1, hue=feature2, ax=axs[0])
        axs[1].set_title("Heatmap showing the relationship between two categorical features")
        axs[1].set_xlabel(feature1)
        axs[1].set_ylabel(feature2)
        sns.heatmap(pd.crosstab(df[feature1], df[feature2]), annot=True, fmt='d', cmap='YlGnBu', ax=axs[1])
        plt.show()

class BivariateAnalyzer(BivariateAnalysisStrategy):
    def __init__(self, strategy: BivariateAnalysisStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: str):
        self.strategy = strategy

    def analyze(self, df:pd.DataFrame, feature1: str, feature2: str):
        self.strategy.analyze(df, feature1, feature2)