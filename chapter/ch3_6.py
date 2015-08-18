# -*- coding: utf-8 -*-
#

import numpy as np
import scipy.stats

# p130 ex1
z1 = scipy.stats.norm.isf(0.025)
e1 = 0.02
p1 = 0.34
n1 = np.power(z1 / e1, 2) * p1 * (1 - p1)

assert np.allclose(int(n1), 2155)
