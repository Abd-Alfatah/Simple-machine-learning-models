import pandas as pd
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
def read():
    """
    read the csv file
    Returns:
        dataframe:returns the tennis balls in the form of pandas data frame
    """
    set_of_data=pd.read_csv("tennis_ball.csv")
    return pd.DataFrame(set_of_data)
time_array=np.array(read()["time"])
hight_array=np.array(read()["hight"])
def predict(time,hight):
    """this fuction build the machine learning model for predicting the hight the ball can
    reach
    Args:
        time (array list):a list of floats
        hight (array list): list of floats that reflect the height the ball reached

    Returns:
        array list: the predicted hieght
    """
    hight_predicted=list()
    a=b=c=0
    n=len(time)
    iterations=5000
    learning_rate=0.04
    for i in range(iterations):
        hight_predicted=(a*time**2+b*time+c)
        cost=(1/n)*sum([val**2 for val in (hight-hight_predicted)])
        ad=-(2/n)*sum(time**2*(hight-hight_predicted))
        bd=-(2/n)*sum((time)*(hight-hight_predicted))
        cd=-(2/n)*sum((hight-hight_predicted))
        a=a-learning_rate*ad
        b=b-learning_rate*bd
        c=c-learning_rate*cd
        print("a: {}, b: {}, c: {}, cost: {},  iteration: {},".format(a,b,c,cost,i))
    return hight_predicted
# ploting the results
#print(time_array)
read().info()
predict(time_array,hight_array)
#print(hight_array)
myline = np.linspace(0, 3, 70)
plt.scatter(read()["time"], read()["hight"])
plt.scatter(time_array,predict(time_array,hight_array))
plt.show()