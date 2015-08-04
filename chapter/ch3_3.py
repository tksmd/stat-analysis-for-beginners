# -*- coding: utf-8 -*-
#
import numpy as np

import scipy.stats


def calc_confidence_interval(data, confidence_coefficient=0.95):
    n = data.size
    mean = data.mean()
    # dislike pandas, numpy's default value of ddof is zero
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html
    var = data.var(ddof=1)
    return calc_confidence_interval_from_values(mean, var, n, confidence_coefficient)


def calc_confidence_interval_from_values(mean, var, n, confidence_coefficient=0.95, use_norm=False):
    a = (1 - confidence_coefficient) / 2
    if use_norm:
        p = scipy.stats.norm.isf(q=a)
    else:
        p = scipy.stats.t.isf(q=a, df=n - 1)
    width = p * np.sqrt(var / n)
    return mean - width, mean + width

# p116 ex1
ex1 = np.array([7.86, 7.89, 7.84, 7.90, 7.82])
start1, end1 = calc_confidence_interval(ex1, 0.99)
assert np.allclose(start1, 7.793, rtol=1.e-4)
assert np.allclose(end1, 7.931, rtol=1.e-4)

# p117 ex2
start2, end2 = calc_confidence_interval_from_values(157.77, 26.419, 60, 0.95, True)
assert np.allclose(start2, 156.47)
assert np.allclose(end2, 159.06, rtol=1.e-4)

# p119 question
x3 = np.array([807, 811, 801, 798, 798, 795, 803, 805, 804])
n3 = x3.size
a3 = ((100 - 99) / 100) / 2
p3 = scipy.stats.t.isf(q=a3, df=n3 - 1)

# manual calculation
mean3 = x3.sum() / n3
x3_squared = x3 * x3
squared_sum = x3_squared.sum()
var3 = (n3 * squared_sum - np.power(x3.sum(), 2)) / (n3 * (n3 - 1))
width3 = p3 * np.sqrt(var3 / n3)
start3 = mean3 - width3
end3 = mean3 + width3

# compare with calcuration using numpy functions
assert start3, end3 == calc_confidence_interval(x3, 0.99)
