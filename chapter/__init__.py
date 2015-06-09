# -*- coding: utf-8 -*-
#
import os
import numpy as np
from pandas import Series

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


def load_text_as_series(file):
    p = os.path.join(DATA_DIR, file)
    if not os.path.exists(p):
        raise ValueError("%s not found" % p)

    return Series(np.loadtxt(p))
