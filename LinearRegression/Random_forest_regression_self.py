# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:12:54 2020

@author: Yash
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load data
dataset = pd.read_csv("Position_Salaries.csv")

X= dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


#fititng Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000, random_state=0)
regressor.fit(X,y)



X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color = 'red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Decision Tree')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()


