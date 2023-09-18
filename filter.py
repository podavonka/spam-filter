from corpus import Corpus
from utils import SPAM_TAG, HAM_TAG
import random
import os

class MyFilter:

    def __init__(self):
        self.is_trained = False

    def train(self, training_dir):
        labels = []

        with open(os.path.join(training_dir, "!truth.txt"), "r", encoding="utf-8") as file:
            content = file.read()
            lines = content.split("\n")
            for line in lines:
                elems = line.split(" ")
                if len(elems) != 2:
                    continue
                labels.append(elems[1])
        # print(labels)
        self.counter = Counter(labels)
        print(self.counter)
        self.is_trained = True

    def test(self, test_dir):
        predictions = {}
        c = Corpus(test_dir)

        for filename, body in c.emails():
            my_prediction = self.classify(body)
            predictions[filename] = my_prediction
            print("E-mail " + filename + "is " + my_prediction)

    def classify(self, body):
        if self.is_trained:
            return self.counter.most_common(1)[0][0]
        else:
            return random.choice(HAM_TAG, SPAM_TAG)

if __name__ == "__main__":
    my_filter = MyFilter()
    # my_filter.train("1")
    # my_filter.test("2")
