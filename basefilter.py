from corpus import Corpus

class BaseFilter:

    def __init__(self):
        pass

    def train(self, training_folder):
        pass

    def classify(self, email_body):
        raise NotImplementedError

    def test(self, test_folder):
        c = Corpus(test_folder)
        predictions = {}

        for filename, email_body in c.emails():
            predictions[filename] = self.classify(email_body)
