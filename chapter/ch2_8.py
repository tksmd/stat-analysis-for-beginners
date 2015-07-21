# -*- coding: utf-8 -*-
#
# F distribution
# http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.f.html
#
import scipy
import scipy.stats
import matplotlib.pyplot as plt

import numpy as np

x = scipy.linspace(0, 6, 100)

fig, axes = plt.subplots(2, 1, figsize=(8, 10))

axes[0].plot(x, scipy.stats.f.pdf(x, 4, 6), label="F(4,6)")
axes[0].plot(x, scipy.stats.f.pdf(x, 10, 10), label="F(10,10)")
axes[0].legend(loc="best", frameon=False)
axes[0].set_title("F distribution of F(4,6) and F(10,10)")

p1 = scipy.stats.f.isf(0.05, 4, 6)
assert np.allclose(p1, 4.5337)

p2 = scipy.stats.f.isf(0.95, 6, 4)
assert np.allclose(p2, 1 / p1)

axes[1].plot(x, scipy.stats.f.pdf(x, 4, 6), label="F(4,6)")
axes[1].plot(x, scipy.stats.f.pdf(x, 6, 4), label="F(6,4)")
axes[1].legend(loc="best", frameon=False)
axes[1].set_title("F(4,6; 0.05) and F(6,4; 0.95)")

axes[1].plot(p1, 0, "k.")
axes[1].plot([p1, p1], [0, scipy.stats.f.pdf(p1, 4, 6)], color="blue", linestyle="dashed")
axes[1].annotate("F(4,6; 0.05)", xy=(p1, 0), xycoords="data",
                 xytext=(-50, 30), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->"))

axes[1].plot(p2, 0, "k.")
axes[1].plot([p2, p2], [0, scipy.stats.f.pdf(p2, 6, 4)], color="green", linestyle="dashed")
axes[1].annotate("F(6,4; 0.95)", xy=(p2, 0), xycoords="data",
                 xytext=(20, 30), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->"))

plt.show()
