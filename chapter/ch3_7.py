# -*- coding: utf-8 -*-
#

import numpy as np
import scipy.stats
import scipy.optimize
from functools import reduce

# MLE
# https://onlinecourses.science.psu.edu/stat504/node/28
#
# MLE for Binomial Distribution
# http://warnercnr.colostate.edu/~gwhite/fw663/BinomialLikelihood.PDF

# p134 ex1
n1 = 8
x1 = [4, 2, 3]


# likelihood function
def lf1(p):
    return reduce(lambda x, y: x * scipy.stats.binom.pmf(y, n=n1, p=p), x1, 1)


# log likelihood function
def llf1(p):
    return np.log(lf1(p))


# negative log likelihood
def nllf1(params):
    return - llf1(params)


r1 = scipy.optimize.minimize_scalar(nllf1, bounds=[0, 1], method="bounded", options={"disp": True})

assert np.allclose(r1.x, 0.375)


# p136 ex2

r2 = scipy.stats.norm.fit([5, 3, 4], fscale=3)
assert np.allclose(r2[0], 4.0)
