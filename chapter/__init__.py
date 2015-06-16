# -*- coding: utf-8 -*-
#
import os
import numpy as np
import pandas as pd
from pandas import Series

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


def load_as_series(txt):
    return Series(np.loadtxt(get_path(txt)))


def load_as_dataframe(csv, opts={}):
    return pd.read_csv(get_path(csv), **opts)


def get_path(file):
    p = os.path.join(DATA_DIR, file)
    if not os.path.exists(p):
        raise ValueError("%s not found" % p)
    return p
