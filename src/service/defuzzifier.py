import numpy as np


def defuzzification(x, mf):
    return center_of_gravity(x, mf)


def center_of_gravity(x, mf) -> float:
    if len(x) != len(mf):
        raise ValueError("The number of items in 'x' does not math with 'mfs'")

    return np.sum(x * mf) / np.sum(mf)


def jaccard_measure(x_mf, y_mf) -> float:
    min_mf = (min(a, b) for a, b in zip(x_mf, y_mf))
    max_mf = (max(a, b) for a, b in zip(x_mf, y_mf))

    return sum(min_mf) / sum(max_mf)