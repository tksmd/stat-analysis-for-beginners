# -*- coding: utf-8 -*-
#

import numpy as np

from pandas import DataFrame
import pandas as pd

import matplotlib.pyplot as plt

from chapter import load_text_as_series

weights = load_text_as_series("ch1_1.txt")

# p14
min_weight = weights.min()
max_weight = weights.max()
data_range = max_weight - min_weight

# Sturges' formula
n = np.ceil(1 + np.log2(weights.size))

# p15

## frequency table
cats = pd.cut(weights, n)
counts = pd.value_counts(cats).sort_index()


def to_int(s):
    return np.ceil(float(s.strip()))


class_values = [(to_int(s) + to_int(e)) // 2 for [s, e] in [v[1:-1].split(",") for v in counts.index]]
df = DataFrame(counts.values, columns=["frequency"], index=class_values)

sample_size = df["frequency"].sum()
df["relative_frequency"] = df["frequency"] / sample_size
df["cum_frequency"] = df["frequency"].cumsum()
df["cum_relative_frequency"] = df["cum_frequency"] / sample_size

## histogram
ax = weights.hist(bins=n)
ax.set_title("Fig 1.1.7 Histogram of Weight")
ax.set_xlabel("Weight")
ax.set_ylabel("Frequency")
plt.show()
