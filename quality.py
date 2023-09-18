from confmat import BinaryConfusionMatrix
from utils import read_classification_from_file

SPAM_TAG = 'SPAM'
HAM_TAG = 'OK'


def quality_score(tp, tn, fp, fn):
    score = (tp + tn) / (tp + tn + 10*fp + fn)
    return score


def compute_quality_for_corpus(corpus_dir):
    cm = BinaryConfusionMatrix(pos_tag=SPAM_TAG, neg_tag=HAM_TAG)
    truth_dict = read_classification_from_file(corpus_dir + '/!truth.txt')
    pred_dict =  read_classification_from_file(corpus_dir + '/!prediction.txt')
    cm.compute_from_dicts(truth_dict, pred_dict)

    cm = cm.as_dict()
    return quality_score(cm['tp'], cm['tn'], cm['fp'], cm['fn'])
