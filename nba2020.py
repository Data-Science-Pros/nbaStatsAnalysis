import pandas as pd
import numpy as np
from math import sqrt,erf

print("Hello, Adam.")

teamStats = pd.read_csv('/Users/adamali/Desktop/nbaPredictor/Data/nbaStats2020.csv')

# print(teamStats)

teamPointsAvg = teamStats.dropna().PTS.mean()
print(teamPointsAvg)

print("The Team Points Average is %.2f" % (teamPointsAvg))
