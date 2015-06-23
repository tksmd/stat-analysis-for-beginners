# -*- coding: utf-8 -*-
#

import scipy
import scipy.stats
import matplotlib.pyplot as plt

from pandas import Series

x = scipy.linspace(0, 10, 11)

ex1 = scipy.stats.hypergeom.pmf(x, M=100, n=100 * 0.1, N=10)
ex2 = scipy.stats.hypergeom.pmf(x, M=1000, n=1000 * 0.5, N=10)

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# bar parameters : http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
data1 = Series(ex1, index=x)
data1.plot(kind="bar", ax=axes[0], title="hyper geometric distribution N=100,n=10,p=0.1", width=1)

data2 = Series(ex2, index=x)
data2.plot(kind="bar", ax=axes[1], title="hyper geometric distribution N=1000,n=10,p=0.5", width=1)

plt.show()
