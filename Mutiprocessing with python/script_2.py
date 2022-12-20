import pandas as pd 
mydataset = {
        'cars': ["BMW","Volvo","Ford"],
        'passing' : [3,7,2]}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)

#series
a = [1,2,3]
myvar =  pd.Series(a)
print(myvar)
print(a[1])

#label
myvar=pd.Series(a, index = ["a","b","c"])
print(myvar)
print(myvar["a"])

calories = {"day1":420,"day2":380,"day3":400}
myvar=pd.Series(calories)
print(myvar)
print(myvar["day1"])

#dataframe
data = {
        "profession" :["student","teacher","police"],
        "age": [21,24,35]}
myvar=pd.DataFrame(data)
print(myvar)
print("the location is\n ",myvar.loc[[0]])