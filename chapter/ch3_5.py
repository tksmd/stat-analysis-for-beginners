# -*- coding: utf-8 -*-
#
import numpy as np

import scipy.stats


def calc_confidence_interval(n, m, confidence_coefficient=0.95):
    a = (1 - confidence_coefficient) / 2
    p = scipy.stats.norm.isf(q=a)
    r = m / n
    width = p * np.sqrt((r * (1 - r)) / n)
    return r - width, r + width

# p126 ex1
start1, end1 = calc_confidence_interval(178, 42)
assert np.allclose(start1, 0.1736, rtol=1.e-3)
assert np.allclose(end1, 0.2983, rtol=1.e-3)


# p127 question
start2, end2 = calc_confidence_interval(54, 37, 0.9)
