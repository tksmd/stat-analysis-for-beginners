# -*- coding: utf-8 -*-
#

from chapter import load_as_series
import numpy as np


class Answer(object):
    def __init__(self, avg, var):
        self.avg = avg
        self.var = var
        self.std_dev = np.sqrt(self.var)

    def __repr__(self):
        return "avg:%.4f variance:%.4f standard deviation:%.4f" % (self.avg, self.var, self.std_dev,)


def calc_stats(samples):
    total = samples.sum()
    powered = samples * samples
    # powered = np.power(samples, 2)
    # powered = samples.apply(lambda x : np.power(x, 2))
    powered_sum = powered.sum()

    n = samples.size
    answer1 = Answer(
        avg=total / n,
        var=(n * powered_sum - total * total) / (n * (n - 1))
    )

    # built-in functions
    # normarized by N-1 as default
    # see http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Series.var.html
    answer2 = Answer(
        avg=samples.mean(),
        var=samples.var()
    )
    return answer1, answer2

# Q1
q1_answer = calc_stats(load_as_series("ch1_2_q1.txt"))
assert q1_answer[0].avg == q1_answer[1].avg
assert q1_answer[0].var == q1_answer[1].var
assert q1_answer[0].std_dev == q1_answer[1].std_dev


# Q2
q2_answer = calc_stats(load_as_series("ch1_2_q2.txt"))
assert q2_answer[0].avg == q2_answer[1].avg
assert q2_answer[0].var == q2_answer[1].var
assert q2_answer[0].std_dev == q2_answer[1].std_dev
