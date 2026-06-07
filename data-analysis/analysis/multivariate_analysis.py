from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MultivariateAnalysisTemplate(ABC):
    """
    Abstract base class that defines a template for performing
    multivariate analysis on a dataset.

    This class follows the Template Method design pattern. The
    `analyze()` method defines the sequence of analysis steps,
    while subclasses implement the specific visualization methods.

    Methods
    -------
    analyze(df, features)
        Executes the complete multivariate analysis workflow.

    generate_pairplot(df, features)
        Generates pairwise relationship visualizations.

    generate_correlation_heatmap(df, features)
        Generates a heatmap representing feature correlations.
    """

    def analyze(self, df: pd.DataFrame, features: list[str]):
        """
        Performs multivariate analysis on the provided dataset.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset containing the features to analyze.

        features : list[str]
            List of feature names to include in the analysis.

        Returns
        -------
        None
            Displays visualizations generated during the analysis.
        """
        self.generate_pairplot(df, features)
        self.generate_correlation_heatmap(df, features)

    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame, features: list[str]):
        """
        Generates a pairplot for the selected features.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset containing the features.

        features : list[str]
            The features to include in the pairplot.

        Returns
        -------
        None
        """
        pass

    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame, features: list[str]):
        """
        Generates a correlation heatmap for the selected features.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset containing the features.

        features : list[str]
            The features to include in the correlation analysis.

        Returns
        -------
        None
        """
        pass


class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    """
    Concrete implementation of the MultivariateAnalysisTemplate.

    This class provides multivariate visualizations using Seaborn:
    - Pairplot for exploring pairwise relationships.
    - Correlation heatmap for analyzing feature correlations.
    """

    def generate_correlation_heatmap(
        self,
        df: pd.DataFrame,
        features: list[str]
    ):
        """
        Generates and displays a correlation heatmap for the
        selected numerical features.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset containing the features.

        features : list[str]
            The features to include in the correlation analysis.

        Returns
        -------
        None
            Displays the generated heatmap.
        """
        numerical_df = df[features].select_dtypes(include="number")
        correlation_matrix = numerical_df.corr()

        plt.figure(figsize=(5, 5))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    def generate_pairplot(
        self,
        df: pd.DataFrame,
        features: list[str]
    ):
        """
        Generates and displays a pairplot for the selected features.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset containing the features.

        features : list[str]
            The features to include in the pairplot.

        Returns
        -------
        None
            Displays the generated pairplot.
        """
        sns.pairplot(df[features])
        plt.suptitle("Pairplot of Selected Features", y=1.02)
        plt.tight_layout()
        plt.show()