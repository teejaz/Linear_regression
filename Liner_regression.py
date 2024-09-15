import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


companies = pd.read_csv('H:/Programing/New folder/1000_Companies.csv')
x =companies.iloc[:, :-1].values
y =companies.iloc[:, 4].values

companies.head()

sns.heatmap(companies.drop('State', axis = 1).corr())
plt.show()