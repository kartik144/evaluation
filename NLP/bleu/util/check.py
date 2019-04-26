def check_total(n):
    """
    Function to check sum of weights
    :param n: list of weights
    :return: true if sum is 1 else 0.
    """
    total = 0

    for x in n:
        total+=x

    if total == 1.0:
        return True
    else:
        return False


def check_type(N):
    """
    Checks if the N-gram parameter type passed is weighted or unweighted.
    Also returns the n-gram or list of weights as required.
    :param N: command line argument for N-gram
    :return: dictionary containing boolean var weighted that tells if the bleu score is to be weighted and the n-gram,
             or list of positional weights for n-grams
    """
    s = [float(x) for x in N.split(",")]
    n = int(s[0]) if len(s) == 1 else tuple(s)
    weighted = not isinstance(n, int)
    return {'weighted': weighted, 'n_gram': n}