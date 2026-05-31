from abc import ABC, abstractmethod
import zipfile
import os
import shutil as shutil
import pandas as pd

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        "Abstract method to ingest data from a given file"
        pass

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        "Method to ingest data from a given zip file."
        if not file_path.endswith('.zip'):
            raise ValueError('The given file is not a zip file')
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")
        
        extracted_files = os.listdir('extracted_data')

        csv_files = [f for f in extracted_files if f.endswith('csv')]

        if len(csv_files) == 0:
            raise FileNotFoundError('No csv files found inside zip file!')
        
        csv_file_path = os.path.join('extracted_data',csv_files[0])
        df = pd.read_csv(csv_file_path)
        shutil.rmtree('extracted_data')
        return df

class DataIngestorFactory(DataIngestor):
    @staticmethod
    def get_data_ingestor(file_extension: str) ->DataIngestor:
        if file_extension == '.zip':
            return ZipDataIngestor()
        else:
            raise ValueError('Unsupported file extension!')

if __name__ == '__main__':
    file_path = '../dataset/archive.zip'
    file_extension = os.path.splitext(file_path)[-1]
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    print(df.head())