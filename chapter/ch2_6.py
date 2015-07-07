# -*- coding: utf-8 -*-
#
# probability functions
# http://www.itl.nist.gov/div898/handbook/eda/section3/eda362.htm

import scipy
import scipy.stats
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.patches import Polygon

# GridSpec http://matplotlib.org/users/gridspec.html
gs = gridspec.GridSpec(3, 3, height_ratios=[2, 1, 1])

x1 = scipy.linspace(0, 10, 100)

# p92
fig = plt.figure(figsize=[12, 10])
ax1 = plt.subplot(gs[0, :-1])
for m in range(1, 7):
    ex1 = scipy.stats.chi2.pdf(x1, df=m)
    ax1.plot(x1, ex1, label="df: %d" % m)
ax1.set_title("chi-square distribution with degree of freedom from 1 to 6")
ax1.legend()

# p93 df:5
x2 = scipy.linspace(0, 16, 100)


def create_patch(a, b, df):
    # http://matplotlib.org/examples/showcase/integral_demo.html
    ix = scipy.linspace(a, b)
    iy = scipy.stats.chi2.pdf(ix, df=df)
    verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
    return Polygon(verts, facecolor='gray', edgecolor='0.9')


def plot_two_side(ax, upper_limit, lower_limit, df):
    ax.plot(x2, scipy.stats.chi2.pdf(x2, df=df))
    ax.add_patch(create_patch(upper_limit, 16, df))
    ax.add_patch(create_patch(0, lower_limit, df))
    ax.set_title("df:%d two-sided alpha:0.025" % df)


def plot_one_tail(ax, limit, is_low, df):
    ax.plot(x2, scipy.stats.chi2.pdf(x2, df=df))
    if is_low:
        ax.add_patch(create_patch(0, limit, df))
    else:
        ax.add_patch(create_patch(limit, 16, df))
    side = "lower" if is_low else "upper"
    ax.set_title("df:%d one-tailed %s side alpha:0.5" % (df, side,))
    ax.set_yticks([])


utp2_1 = scipy.stats.chi2.isf(q=0.025, df=5)
assert np.allclose(utp2_1, 12.8325)
ltp2_1 = scipy.stats.chi2.ppf(q=0.025, df=5)
assert np.allclose(ltp2_1, 0.831212)
ax2 = plt.subplot(gs[1, 0])
plot_two_side(ax2, utp2_1, ltp2_1, 5)

utp2_2 = scipy.stats.chi2.isf(q=0.05, df=5)
assert np.allclose(utp2_2, 11.0705)
ax3 = plt.subplot(gs[1, 1])
plot_one_tail(ax3, utp2_2, False, 5)

ltp2_2 = scipy.stats.chi2.ppf(q=0.05, df=5)
assert np.allclose(ltp2_2, 1.145476)
ax4 = plt.subplot(gs[1, 2])
plot_one_tail(ax4, ltp2_2, True, 5)

# p93 df:6
utp3_1 = scipy.stats.chi2.isf(q=0.025, df=6)
assert np.allclose(utp3_1, 14.4494)
ltp3_1 = scipy.stats.chi2.ppf(q=0.025, df=6)
assert np.allclose(ltp3_1, 1.237344)
ax5 = plt.subplot(gs[2, 0])
plot_two_side(ax5, utp3_1, ltp3_1, 6)

utp3_2 = scipy.stats.chi2.isf(q=0.05, df=6)
assert np.allclose(utp3_2, 12.5916)
ax6 = plt.subplot(gs[2, 1])
plot_one_tail(ax6, utp3_2, False, 6)

ltp3_2 = scipy.stats.chi2.ppf(q=0.05, df=6)
assert np.allclose(ltp3_2, 1.63538)
ax7 = plt.subplot(gs[2, 2])
plot_one_tail(ax7, ltp3_2, True, 6)

plt.show()
