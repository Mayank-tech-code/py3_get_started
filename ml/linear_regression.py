#Credits: https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d

import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r'data\data1.csv')
X = data.iloc[:, 0].values.reshape(-1, 1)
Y = data.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()
