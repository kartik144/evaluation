class Counter(object):
    """
    Counter class to track true positives and false positives and get precision
    """
    def __init__(self):
        self.true_positive = 0
        self.false_positive = 0

    def update_true_positive(self):
        self.true_positive += 1

    def update_false_positive(self):
        self.false_positive += 1

    def get_precision(self):
        precision = self.true_positive / (self.true_positive + self.false_positive)
        return precision