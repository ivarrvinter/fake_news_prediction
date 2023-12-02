from FileManager import FileManager
from TextProcessor import TextProcessor
from DataProcessor import DataProcessor

file_path = '/kaggle/input/fake-news/news.csv'

class MainScript:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_manager = FileManager()
        self.text_processor = TextProcessor()
        self.data_processor = DataProcessor()

    def process_data(self):
        # Read CSV file
        df = self.file_manager.read_csv(self.file_path)

        # Initialize target column
        df['target'] = self.data_processor.binarize_labels(df['label'])

        # Drop unnecessary columns
        df = self.data_processor.drop_columns(df)

        # Apply lowercase to title and text columns
        df['title'] = df['title'].apply(self.text_processor.lowercase)
        df['text'] = df['text'].apply(self.text_processor.lowercase)

        # Lemmatize title and text columns
        df['title_lemma'] = df['title'].apply(self.text_processor.lemmatize)
        df['text_lemma'] = df['text'].apply(self.text_processor.lemmatize)

        return df

# Instantiate and execute
main_script = MainScript(file_path)
processed_data = main_script.process_data()
