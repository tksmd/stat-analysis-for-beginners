# -*- coding: utf-8 -*-
#

from chapter import load_as_dataframe

df = load_as_dataframe("ch1_5.csv", {
    "index_col": "traffic accident"
})

p = df["without seat belt"]["dead"] / df["without seat belt"].sum()
q = df["with seat belt"]["dead"] / df["with seat belt"].sum()

p_odds = p / (1 - p)
q_odds = q / (1 - q)

odds_ratio1 = p_odds / q_odds

# odds_ratio = ( a/b ) / ( c/d )
odds_ratio2 = (df["without seat belt"]["dead"] * df["with seat belt"]["alive"]) / \
              (df["with seat belt"]["dead"] * df["without seat belt"]["alive"])

print("odds ratio 1 : %.4f" % odds_ratio1)
print("odds ratio 2 : %.4f" % odds_ratio2)
