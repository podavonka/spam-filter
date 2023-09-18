from basefilter import BaseFilter
from utils import SPAM_TAG, HAM_TAG


class NaiveFilter(BaseFilter):
    """OK"""
    def classify(self, email_body):
        return

class ParanoidFilter:
   """SPAM"""
    def __init__(self):
        pass

class RandomFilter:

    def __init__(self):
        pass

