from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
Abstract Base Class for missing value analysis and visulization
"""
class MissingValueAnalysis(ABC):
    def analyze(self, df: pd.DataFrame) -> None:
        """
        Analyze the missing values that are present in the dataset and visulize them as well.

        Parameters:
        df (pd.DataFrame) : Dataset that is to be analyzed for missing values
        Returns:
        None : Returns nothing only prints the visulizations and the missing values that are identified
        """
        self.identify_missing_values(df)
        self.visulize_missing_values(df)
    
    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame)-> None:
        """
        Abstract Method for the implementation of missing values identification
        Parameters:
        df (pd.DataFrame) : Input Dataset
        Returns:
        None : Just identifies missing values and print the results as it is.
        """
        pass

    @abstractmethod
    def visulize_missing_values(self, df: pd.DataFrame)->None:
        """
        Abstract method for visulization of missing values.
        Parameters:
        df (pd.DataFrame) : The dataset to for which the missing values is to be visulized after identification
        Returns:
        None : Only prints the visulizations
        """
        pass

class MissingValueAnalyzer(MissingValueAnalysis):
    def identify_missing_values(self, df: pd.DataFrame) -> None:
        """
        Method for concrete implementation of missing values identification.
        Parameters:
        df (pd.DataFrame): Input Dataset for missing values identification
        Returns:
        None : Just identifies missing values in the given dataset and prints the results
        directly
        """
        print('Identify Missing Values...')
        print('Missing Values Info')
        missing_values_info = df.isnull().sum()
        print(missing_values_info[missing_values_info > 0])

    def visulize_missing_values(self, df: pd.DataFrame) -> None:
        """
        Method for concrete implementation of missing values visualization.
        Parameters:
        df (pd.DataFrame): Input Dataset for missing values visulization.
        Returns:
        None : Performs visulizations on the missing values and prints the results directly
        
        """
        plt.figure(figsize=(10,10))
        sns.heatmap(df.isnull(),cmap='viridis')
        plt.title("Missing Values Heatmap")
        plt.show()