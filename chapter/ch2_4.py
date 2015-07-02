# -*- coding: utf-8 -*-
#

import scipy
import scipy.stats
import matplotlib.pyplot as plt

from pandas import Series

x1 = scipy.linspace(0, 6, 7)

ex1 = scipy.stats.poisson.pmf(x1, mu=1)

# https://en.wikipedia.org/wiki/Poisson_distribution
data1 = Series(ex1, index=x1)
fig, ax = plt.subplots(1, 1)
data1.plot(kind="bar", ax=ax, title="Poisson distribution lambda=1", width=1)
plt.show()

# the number of soldiers in the Prussian army killed accidentally by horse kicks; by Bortkewitsch
x2 = scipy.linspace(0, 4, 5)
ex2 = scipy.stats.poisson.pmf(x2, mu=0.61)
data2 = Series(ex2, index=x2)
