"""Definition of the evaluation metrics.

This module contains the definition of the evaluation metrics `average precision` and `mean average precision`.
"""


import numpy as np


def ap(recommended, rated, trunc=10):
    """Calculate truncated average precision.
    
    :param recommended: recommended items of one user
    :param rated: rated items of one user
    :param trunc: truncation
    :return: average precision
    """
    trunc = min(len(recommended), trunc)
    rank = 0
    avg_pre = 0
    for i in range(trunc):
        if recommended[i] in rated:
            rank += 1
            avg_pre += rank / (i + 1)
    avg_pre /= trunc
    return avg_pre


def mean_ap(recommended_items, rated_items, trunc=10):
    """Calculate truncated mean average precision
    
    :param recommended_items: recommended items of all users
    :param rated_items: rated items of all users
    :param trunc: truncation
    :return: mean average precision
    """
    mean_avg_pre = np.mean([ap(recommended, rated_items[user], trunc)
                            for user, recommended in recommended_items.items()])
    return mean_avg_pre
