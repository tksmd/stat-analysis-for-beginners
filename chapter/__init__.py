# -*- coding: utf-8 -*-
#
import os
import numpy as np
import pandas as pd
from pandas import Series

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


def load_as_series(txt):
    p = os.path.join(DATA_DIR, txt)
    if not os.path.exists(p):
        raise ValueError("%s not found" % p)

    return Series(np.loadtxt(p))


def load_as_dataframe(csv):
    p = os.path.join(DATA_DIR, csv)
    if not os.path.exists(p):
        raise ValueError("%s not found" % p)

    return pd.read_csv(p)
