'''
Problem Statement Link:
https://medium.com/analytics-vidhya/linear-regression-using-pandas-numpy-for-beginners-in-data-science-fe57157ed93d
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
 
 
# Read the file
 
cust = pd.read_csv("Ecommerce Customers.csv")
 
# Let’s checkout the data -
 
print(cust.head())
 
print("No of Rows =" , cust.shape)
'''
sns.jointplot(x='Time on Website',y='Yearly Amount Spent', data=cust)
plt.show()
 
sns.jointplot(x='Time on App',y='Yearly Amount Spent', data=cust)
plt.show()
 
 
sns.pairplot(data=cust)
plt.show()
'''
 
sns.jointplot(x='Length of Membership',y='Yearly Amount Spent',data=cust)
plt.show()
 
 
X =cust[['Avg. Session Length','Time on App','Time on Website','Length of Membership']]
 
Y=cust['Yearly Amount Spent']
 
 
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2,random_state=10)
 
 
lm = LinearRegression()
 
 
lm.fit(X_train,Y_train)
 
 
print(lm.coef_)