from sklearn.preprocessing import LabelBinarizer

class DataProcessor:
    def __init__(self):
        self.lb = LabelBinarizer()
        self.columns_to_drop = ['Unnamed: 0', 'label']
    
    def binarize_labels(self, labels):
        self.lb.fit(['FAKE', 'REAL'])
        return self.lb.transform(labels)
    
    def drop_columns(self, df):
        return df.drop(self.columns_to_drop, axis=1)
