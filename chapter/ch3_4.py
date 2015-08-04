# -*- coding: utf-8 -*-
#
import numpy as np

import scipy.stats


def calc_confidence_interval(data, confidence_coefficient=0.95):
    n = data.size
    upper = (1 - confidence_coefficient) / 2
    lower = 1 - upper
    var = data.var(ddof=1)
    numerator = (n - 1) * var
    return numerator / scipy.stats.chi2.isf(q=upper, df=n - 1), \
           numerator / scipy.stats.chi2.isf(q=lower, df=n - 1)

# p122 ex1
ex1 = np.array([4.9, -2.6, 3.1, -1.2, 6.4, -3.5])
start1, end1 = calc_confidence_interval(ex1)
assert np.allclose(start1, 6.751, rtol=1.e-4)
assert np.allclose(end1, 104.22, rtol=1.e-4)

# p123 question
x2 = np.array([15.4, 16.1, 15.7, 16.6, 14.9, 15.5, 16.2])
a2 = ((100 - 95) / 100) / 2
n2 = x2.size
chi2_upper2 = scipy.stats.chi2.isf(q=a2, df=n2 - 1)
chi2_lower2 = scipy.stats.chi2.isf(q=1 - a2, df=n2 - 1)

# manual calculation
x2_squared = x2 * x2
squared_sum = x2_squared.sum()
var2 = (n2 * squared_sum - np.power(x2.sum(), 2)) / (n2 * (n2 - 1))

start2 = ((n2 - 1) * var2) / chi2_upper2
end2 = ((n2 - 1) * var2) / chi2_lower2

# compare with calcuration using numpy functions
assert start2, end2 == calc_confidence_interval(x2, 0.95)
