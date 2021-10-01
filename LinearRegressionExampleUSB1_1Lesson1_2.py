# Sklearn module
# Rough outline of regular sklearn code in regular coding.
from sklearn.linear_model import Linear Regression
import pandas as pd
X, y = pd.read_csv(“house_csv”)
#preprocessing...
Linreg = LinearRegression()
Linreg.fit(X, y)
Linreg.predict(Xtr)
