def pos_to_one_hot(n):
    """
    Helper function to convert positional index to one-hot array
    :param n:
    :return o: one-hot array
    """

    o = [0] * n
    o[n-1] = 1
    return tuple(o)