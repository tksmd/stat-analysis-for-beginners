# -*- coding: utf-8 -*-
#

from itertools import combinations

from chapter import load_as_dataframe

df = load_as_dataframe("ch1_4.csv", {
    "index_col": "generation"
})

pairs = [df[list(p)] for p in combinations(df.columns, 2)]


def direction_filter(positive):
    def f(pair):
        v = (pair.ix[:, 0] - pair.ix[:, 1]).prod()
        return v > 0 if positive else v < 0

    return f


P = sum(1 for _ in filter(direction_filter(True), pairs))
Q = sum(1 for _ in filter(direction_filter(False), pairs))
# Kendall tau rank correlation coefficient
tau = (P - Q) / len(pairs)
