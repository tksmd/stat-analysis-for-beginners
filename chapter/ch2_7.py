# -*- coding: utf-8 -*-
#
# probability functions
# http://www.itl.nist.gov/div898/handbook/eda/section3/eda362.htm

import scipy
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import numpy as np
from matplotlib.patches import Polygon

gs = gridspec.GridSpec(2, 4, height_ratios=[5, 3])

x1 = scipy.linspace(-3, 3, 100)
fig = plt.figure(figsize=[12, 10])
ax1 = plt.subplot(gs[0, :-2])

for m in [1, 2, 5, 100]:
    ex1 = scipy.stats.t.pdf(x1, m)
    ax1.plot(x1, ex1, label="df: %d" % m)
ax1.legend()
ax1.set_title("t distribution with degree of freedom 1,2,5,100")

# comparison with normal distribution
ax2 = plt.subplot(gs[0, -2:])
ax2.plot(x1, scipy.stats.t.pdf(x1, 5), label="t(df:5)")
ax2.plot(x1, scipy.stats.norm.pdf(x1, loc=0, scale=np.sqrt(5 / 3)), label="N(0,5/3)")
ax2.plot(x1, scipy.stats.t.pdf(x1, 30), label="t(df:30)")
ax2.plot(x1, scipy.stats.norm.pdf(x1, loc=0, scale=np.sqrt(30 / 28)), label="N(0,30/28)")
ax2.legend()
ax2.set_title("comparison with normal distribution")

# p96
def create_patch(a, b, df):
    # http://matplotlib.org/examples/showcase/integral_demo.html
    ix = scipy.linspace(a, b)
    iy = scipy.stats.t.pdf(ix, df=df)
    verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
    return Polygon(verts, facecolor='gray', edgecolor='0.9')


def plot_two_side(ax, limit, df):
    ax.plot(x1, scipy.stats.t.pdf(x1, df=df))
    ax.add_patch(create_patch(limit, 3, df))
    ax.add_patch(create_patch(-3, -limit, df))
    ax.set_title("df:%d alpha:0.025" % df)


def plot_one_tail(ax, limit, df):
    ax.plot(x1, scipy.stats.t.pdf(x1, df=df))
    ax.add_patch(create_patch(limit, 3, df))
    ax.set_title("df:%d alpha:0.5" % df)


ax3 = plt.subplot(gs[1, 0])
ul3 = scipy.stats.t.isf(0.025, 5)
plot_two_side(ax3, ul3, 5)

ax4 = plt.subplot(gs[1, 1])
ul4 = scipy.stats.t.isf(0.05, 5)
plot_one_tail(ax4, ul4, 5)
ax4.set_yticks([])

ax5 = plt.subplot(gs[1, 2])
ul5 = scipy.stats.t.isf(0.025, 10)
plot_two_side(ax5, ul5, 10)

ax6 = plt.subplot(gs[1, 3])
ul6 = scipy.stats.t.isf(0.05, 10)
plot_one_tail(ax6, ul6, 10)
ax6.set_yticks([])

plt.show()
