# -*- coding: utf-8 -*-
#

from scipy.stats import chi2, t, f
import numpy as np

# Q1
q1_1 = chi2.isf(q=0.95, df=4)
assert np.allclose(q1_1, 0.710723)
q1_2 = chi2.isf(q=0.05, df=4)
assert np.allclose(q1_2, 9.48773)
q1_3 = chi2.isf(q=0.95, df=9)
assert np.allclose(q1_3, 3.32511)
q1_4 = chi2.isf(q=0.05, df=9)
assert np.allclose(q1_4, 16.9190)

# Q2
q2_1 = t.isf(q=0.05, df=7)
assert np.allclose(q2_1, 1.895, rtol=1.e-3)
q2_2 = t.isf(q=0.025, df=7)
assert np.allclose(q2_2, 2.365, rtol=1.e-3)
q2_3 = t.isf(q=0.05, df=12)
assert np.allclose(q2_3, 1.782, rtol=1.e-3)
q2_4 = t.isf(q=0.025, df=12)
assert np.allclose(q2_4, 2.179, rtol=1.e-3)

# Q3
q3_1 = f.isf(q=0.05, dfn=5, dfd=7)
assert np.allclose(q3_1, 3.9715)
q3_2 = f.isf(q=0.95, dfn=5, dfd=7)
assert np.allclose(q3_2, 0.2050903422957813)  # inverse of F(7,5; 0.05)
