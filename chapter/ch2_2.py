# -*- coding: utf-8 -*-
#

import scipy
import scipy.stats
import matplotlib.pyplot as plt

from pandas import Series

x = scipy.linspace(0, 10, 11)

ex1 = scipy.stats.binom.pmf(x, n=10, p=0.5)
ex2 = scipy.stats.binom.pmf(x, n=10, p=0.1)

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# bar parameters : http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
data1 = Series(ex1, index=x)
data1.plot(kind="bar", ax=axes[0], title="binomial distribution B(10,0.5)", width=1)

data2 = Series(ex2, index=x)
data2.plot(kind="bar", ax=axes[1], title="binomial distribution B(10,0.1)", width=1)

plt.show()
