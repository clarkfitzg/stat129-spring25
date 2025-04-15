from math import exp


def exp_cdf(x):
    """Calculate the cumulative distribution function
        F(x) for X ~ exponential(1)
    """
    return 1 - exp(-x)


xx = [0, 1, 2, 4]
