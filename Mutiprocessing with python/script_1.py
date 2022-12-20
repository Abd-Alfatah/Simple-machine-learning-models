import pandas as pd
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
#def readingDatas():
longitudinal_dynamics_model=pd.read_excel("Different parameters.xlsx")
    #return longitudinal_dynamics_model
for i in range(49):
    if longitudinal_dynamics_model.loc[i,"length_from_rear_tire_to_centre"]<1:
        longitudinal_dynamics_model.loc[i,"length_from_rear_tire_to_centre"]=longitudinal_dynamics_model["length_from_rear_tire_to_centre"].mean()
#readingDatas()["length_from_rear_tire_to_centre"].fillna(value=readingDatas()["length_from_rear_tire_to_centre"].mean(), inplace=True)
#readingDatas()["length_from_rear_tire_to_centre"].replace(readingDatas()["length_from_rear_tire_to_centre"].mean(), inplace=True)
print(longitudinal_dynamics_model["length_from_rear_tire_to_centre"].mean())
longitudinal_dynamics_model.info()
print(longitudinal_dynamics_model["length_from_rear_tire_to_centre"].to_string())
print(longitudinal_dynamics_model.corr())
longitudinal_dynamics_model.plot(x="Wf (KN)", y="Wr (KN)")
plt.show()