from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df:pd.DataFrame, feature: str):
        """
        Performs Univariate Analysis on the specified feature of the DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature (str): The name of the feature/column to analyze.
        """
        pass

class NumericalUnivariateStrategy(UnivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature: str):
        """
        Performs Univariate analysis on the specified numerical feature of the DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature (str): The name of the feature/column to analyze.
        """
        plt.figure(figsize=(5,5))
        plt.title('Plot showing the distribution of numerical feature')
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        sns.histplot(data=df, x = feature, kde=True, bins=30)
        plt.show()

class CategoricalUnivariateStrategy(UnivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Performs bivariate analysis on specified categorical feature of DataFrame.
        Parameters:
        df (pd.DataFrame): The input DataFrame containing the data.
        feature (str): The name of the feature/column to analyze.
        """
        plt.figure(figsize=(5,5))
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        sns.countplot(data=df, x=feature)
        plt.tight_layout()
        plt.show()

class UnivariateAnalyzer(UnivariateAnalysisStrategy):
    """
    Context class for performing univariate analysis using different strategies.
    Parameters:
    strategy (UnivariateAnalysisStrategy): The strategy to use for univariate analysis.
    """
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        self.strategy = strategy

    def analyze(self, df: pd.DataFrame, feature: str):
        self.strategy.analyze(df, feature)