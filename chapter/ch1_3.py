# -*- coding: utf-8 -*-
#

from chapter import load_as_dataframe

import numpy as np

import matplotlib.pyplot as plt


class Answer(object):
    def __init__(self, corr, var_x, var_y, cov):
        self.corr = corr
        self.var_x = var_x
        self.var_y = var_y
        self.cov = cov

    def __repr__(self):
        fmt = "correlation coefficient: %.4f variance x: %.4f variance y: %.4f covariance xy: %.4f"
        return fmt % (self.corr, self.var_x, self.var_y, self.cov,)

    def val(self):
        return self.corr, self.var_x, self.var_y, self.cov,


def calc_stats(df):
    df["xpower"] = df["x"] * df["x"]
    df["ypower"] = df["y"] * df["y"]
    df["xy"] = df["x"] * df["y"]

    n = df.index.size
    denom = n * (n - 1)

    x_numer = n * df["xpower"].sum() - np.power(df["x"].sum(), 2)
    y_numer = n * df["ypower"].sum() - np.power(df["y"].sum(), 2)
    cov_numer = n * df["xy"].sum() - df["x"].sum() * df["y"].sum()

    corr = cov_numer / (np.sqrt(x_numer) * np.sqrt(y_numer))
    var_x = x_numer / denom
    var_y = y_numer / denom
    cov_xy = cov_numer / denom

    answer1 = Answer(
        corr=cov_numer / (np.sqrt(x_numer) * np.sqrt(y_numer)),
        var_x=x_numer / denom,
        var_y=y_numer / denom,
        cov=cov_xy,
    )

    # built-in functions
    answer2 = Answer(
        corr=df["x"].corr(df["y"]),
        var_x=df["x"].var(),
        var_y=df["y"].var(),
        cov=df["x"].cov(df["y"]),
    )

    return answer1, answer2

# Q1
df1 = load_as_dataframe("ch1_3_q1.csv")
q1_answer = calc_stats(df1)
assert np.allclose(q1_answer[0].val(), q1_answer[1].val())

# Q2
df2 = load_as_dataframe("ch1_3_q2.csv")
q2_answer = calc_stats(df2)
assert np.allclose(q2_answer[0].val(), q2_answer[1].val())

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(121)
ax1.scatter(df1["x"], df1["y"], color='blue', s=5, edgecolor='none')
ax1.set_aspect(1. / ax1.get_data_ratio())
ax1.set_title("Fig 1.3.10")
ax1.set_xlabel("price")
ax1.set_ylabel("maximum output")

ax2 = fig.add_subplot(122)
ax2.scatter(df2["x"], df2["y"], color='red', s=5, edgecolor='none')
ax2.set_aspect(1. / ax2.get_data_ratio())
ax2.set_title("Fig 1.3.11")
ax2.set_xlabel("medical examination rate")
ax2.set_ylabel("death rate")

plt.show()
