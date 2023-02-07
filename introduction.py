import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("gapminder-FiveYearData.csv")
'''
print(
    df.head(),
    "\n",
    df.info(),
    "\n",
    df.head(),
    "\n",
    df.tail(1)
)
'''
country_df = df['country']

print(
    country_df.head(),
    "\n",
    country_df.info(),
    "\n",
    country_df.head(),
    "\n",
    country_df.tail(1)
)

print(df.iloc[-1])