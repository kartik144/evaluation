import argparse
from nltk.translate.bleu_score import sentence_bleu
from util.check import *
from util.misc import *
from counter import Counter


def get_bleu_scores(input, ref, threshold, n):
    """
    Returns per-instance bleu score and average bleu score.
    :param input: Path to input file
    :param ref: Path to reference file
    :param threshold: Threshold of blue score to consider an input as true positive
    :param n: n_grams/weights to consider
    :return: list of individual bleu scores and average bleu score
    """
    f_input = open(input, "r")
    f_ref = open(ref, "r")
    scores = []
    true_positives = []
    total_score = 0
    count = 0
    counter = Counter()

    for candidate in f_input:
        reference = [f_ref.readline()]
        score = sentence_bleu(reference, candidate, weights=n)
        scores.append(score)
        total_score += score
        count += 1

        if score > threshold:
            true_positives.append(True)
            counter.update_true_positive()
        else:
            true_positives.append(False)
            counter.update_false_positive()

    avg_score = total_score/count
    f_input.close()
    f_ref.close()

    return {'scores': scores,
            'average_score': avg_score,
            'true_positives': true_positives,
            'precision': counter.get_precision()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", default="1", help="N-gram (e.g. 1/2/3... or \"0.25,0.25,0.5\" "
                                                "in case of weighted bleu score)")
    parser.add_argument("-T", default=0.5, type=float, help="Threshold")
    parser.add_argument("--input", default="./data/test/input.txt", help= "Path to input file")
    parser.add_argument("--reference", default="./data/test/reference.txt", help= "Path to reference file")

    args = parser.parse_args()

    temp = check_type(args.N)
    weighted = temp['weighted']
    n = temp['n_gram']
    n = pos_to_one_hot(n) if not weighted else n

    if weighted and not check_total(n):
            raise Exception('Sum of weights should be equal to 1.0')

    res = get_bleu_scores(args.input, args.reference, args.T, n)
    print(res)
