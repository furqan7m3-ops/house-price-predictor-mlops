from abc import ABC, abstractmethod
import pandas as pd
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection
        Parameters:
        df (pd.DataFrame) : The dataframe on which the inspection is applied

        Returns:
        None :  This method prints the inspection results directly

        """
        pass

class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df):
        """
        A method that performs data types inspections and prints non null counts in each column
        Parameters:
        df (pd.DataFrame) : The dataset on which the analysis will be performed
        
        Returns:
        None : Prints the Results (Datatypes along with non-null counts) directly
        """
        print(df.info())


class SummaryStatisticsStrategy(DataInspectionStrategy):
    def inspect(self, df):
        """
        A method that performs data types inspections and prints non null counts in each column
        Parameters:
        df (pd.DataFrame) : The dataset on which the analysis will be performed
        
        Returns:
        None : Prints the Results (Datatypes along with non-null counts) directly
        """
        print('Summary Statistics')
        print('-------------------')
        print('For Numerical Attributes')
        print(df.describe())
        print()
        print('For Categorical Attributes:')
        print(df.describe(include=['O']))

class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: DataInspectionStrategy):
        self.strategy = strategy
        
    def execute_inspection(self, df: pd.DataFrame):
        self.strategy.inspect(df)