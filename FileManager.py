import pandas as pd

class FileManager:
    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)
