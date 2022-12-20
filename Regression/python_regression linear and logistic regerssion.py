#Abd-Alfatah Alodain
#UA3AGW
# import  the required libraries
import pandas as pd
import math as m
import matplotlib.pyplot as plt
#Read and set the data
set_of_data=pd.read_csv("Hungarian_Heart_Disease.csv")
set_of_data=set_of_data.dropna()
set_of_data=pd.DataFrame(set_of_data)
#return pd.DataFrame(set_of_data)
#extracting the info of the csv file
# now we will clean the data 
for column in set_of_data:
    for i in set_of_data.index:
        if set_of_data.loc[i,column] <0:
            if set_of_data[column].mean()>0:
                set_of_data.loc[i,column] =m.ceil(set_of_data[column].mean())#return the higher value
            else:
                set_of_data.loc[i,column] =m.floor(set_of_data[column].max())        
# show the relations to start the regression
print(set_of_data)
set_of_data.info()
print(set_of_data.corr())## to show which data has a big effect on the result
set_of_data.plot(kind="scatter",x="thal",y="predicted attribute") 
# ploting the data to get to know the nature of the result
plt.show()
# After we did data cleaning we can now preform the regression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
# we will preform linear regression only for the values that has a big relation to the output
# from above data we can see that the ones that have this big corr are cp,exang and oldpeak
#lets start with Linear regression, single and mutiple
import numpy as np
X=pd.DataFrame(np.c_[set_of_data["thalach"],set_of_data["Age"],set_of_data["Sex"],set_of_data["exang"],set_of_data["oldpeak"],set_of_data["cp"]],columns=["thalach","Age","Sex","exang","oldpeak","cp"])
Y=set_of_data["predicted attribute"]
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2, random_state=1)
linear_reg_mod= LinearRegression()
linear_reg_mod.fit(X_train, y_train)
predicted= linear_reg_mod.predict(X_test)
test_set_rmse= np.sqrt (mean_squared_error( y_test, predicted)) 
test_set_r2 = r2_score(y_test, predicted)
print("test_set_rmse: " , test_set_rmse)
print("test_set_r2: ", test_set_r2)
""" outputs are as folllows
test_set_rmse:  0.8909317434044535
test_set_r2:  0.5099190542988226
"""
###Now let us preform the logistic Regression
from sklearn.linear_model import LogisticRegression
logistic_regression= LogisticRegression()
logistic_regression.fit(X_train, y_train)
predicted= logistic_regression.predict(X_test)
test_set_rmse= np.sqrt (mean_squared_error( y_test, predicted)) 
test_set_r2 = r2_score(y_test, predicted)
print("test_set_rmse for logistic: " , test_set_rmse)
print("test_set_r2for logistic: ", test_set_r2)
"""outputs are the following
test_set_rmse for logistic:  0.7919082295744858
test_set_r2for logistic:  0.6128059595601276 
"""