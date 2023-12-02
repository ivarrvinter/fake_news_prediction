import spacy

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def lowercase(self, text):
        return text.lower()

    def lemmatize(self, text):
        doc = self.nlp(text)
        if doc.has_annotation("DEP"):
            return [token.lemma_ for token in doc]
        else:
            return None
