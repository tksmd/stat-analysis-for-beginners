# -*- coding: utf-8 -*-
#
import scipy
import scipy.stats
from scipy.stats import norm
import matplotlib.pyplot as plt

from pandas import Series
import numpy as np

from chapter import load_as_dataframe

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# p81
# normal distribution parameters loc:mean, scale:standard deviation
params1 = {
    "loc": 0,
    "scale": 1,
}
# http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.norm.html
x1 = scipy.linspace(norm.ppf(0.001, **params1), norm.ppf(0.999, **params1), 1000)
ex1 = norm.pdf(x1, **params1)

data1 = Series(ex1, index=x1)
data1.plot(title="Normal distribution N(0,1^2)", ax=axes[0][0])

# p85
df2 = load_as_dataframe("ch2_5.csv", {
    "index_col": "no"
})
height2 = df2["height"]
n2 = np.ceil(1 + np.log2(height2.size))
height2.hist(bins=n2, ax=axes[1][0], normed=True)
height2.plot(kind='kde', ax=axes[1][0], title="KDE and Normal distribution for heights")
params2 = {
    "loc": height2.mean(),
    "scale": np.sqrt(height2.var())
}
x2 = scipy.linspace(norm.ppf(0.001, **params2), norm.ppf(0.999, **params2), 1000)
ex2 = norm.pdf(x2, **params2)
data2 = Series(ex2, index=x2)
data2.plot(ax=axes[1][0])

# p87
params3 = {
    "loc": 157.77,
    "scale": 5.14
}


def normalize(value, params):
    return (value - params["loc"]) / params["scale"]

# Cumulative Distribution Function : http://www.itl.nist.gov/div898/handbook/eda/section3/eda362.htm
not_normed = norm.cdf([150, 160], **params3)
p3_1 = not_normed[1] - not_normed[0]
normed = norm.cdf([normalize(x, params3) for x in [150, 160]])
p3_2 = normed[1] - normed[0]
np.allclose(p3_1, p3_2)

# p88
p4_binom = scipy.stats.binom.pmf(6, n=10, p=0.5)
params4 = {
    "loc": 10 * 0.5,
    "scale": np.sqrt(10 * 0.5 * (1 - 0.5))
}
norm4 = norm.cdf([5.5, 6.5], **params4)
p4_norm = norm4[1] - norm4[0]
x4 = scipy.linspace(0, 10, 11)
data4_norm = Series(norm.pdf(x4, **params4), index=x4)
data4_norm.plot(ax=axes[0][1], kind="bar", width=1,
                title="B(10,0.5) and N(%.0f, %0.2f)" % (params4["loc"], params4["scale"]))
data4_binom = Series(scipy.stats.binom.pmf(x4, n=10, p=0.5), index=x4)
data4_binom.plot(ax=axes[0][1], color="r")

# p90
means_5 = []
for _ in range(200):
    samples = np.random.standard_t(5, 10)
    means_5.append(samples.mean())

data5 = Series(means_5)
n5 = np.ceil(1 + np.log2(data5.size))
axes[1][1].set_title("Random samples with mean 0, variance 1.67")
data5.hist(bins=n5, ax=axes[1][1], normed=True)

plt.show()
