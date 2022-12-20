""" Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]"""
import multiprocessing as mp # HERE WE IMPORTED THE LIBRARY FOR PARALLISATION 
import os# This library is imported, so we are able to operate with our
          #system (using files in our directories)
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]#assining values to list a and b
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
def get_row_wise():#This function will return the new list, which contain the common 
    #Elements in list a and lsit b
    global list_c #defining a list c
    list_c= [[x for x in a if x in b]for a, b in zip(list_a, map(set, list_b))]
    #we will chick if x is in a and b at the same time, if so we put it in the new lis
    #a and b are the tuples taken one by one from list_a and list_b
    #zip function will map through the elements in the lists a,b
    return list_c 
####################################################################
#task 2
def run_the_process(process):#This funxtion will run the required files
    os.system('python {}'.format(process))#using os module we will run the required files
###################################################################################
#task 3 Normalize each row of 2d array (list) to vary between 0 and 1.
def normalize(mylist):# this function will normalize our lists
    mini = min(mylist)# here we are looking for the maximum
    maxi = max(mylist)#here we are looking for the minimum
    return [(i - mini)/(maxi-mini) for i in mylist]#NORMALIZED LIST
if __name__=="__main__":#check is we are in the main and perform the operations
    #this step is required because parallellsim does not operate with links with out this function
    with mp.Pool(4) as pool:#calling the 4 process
        result = [pool.apply(get_row_wise) ]#for task 1
        print(result)#print the  result
        #ouptuts  [[[2, 3], [6], [11, 12], [21]]]
        processes = ('script_1.py', 'script_2.py', 'parallel.py')#second task
        pool.map(run_the_process,processes)# calling the function for the seconed task
        #All the previous files will run and we are going to seen the outputs of the files in the console screen
        normalized_list=[pool.apply(normalize, args=(l,)) for l in list_a]#third task
        pool.close()# closing or stopping the multiprocessing operation
        print(normalized_list)#print result
        #outputs
        # [[0.0, 0.5, 1.0], [0.0, 0.3333333333333333, 0.6666666666666666, 1.0], [0.0, 0.5, 1.0], [0.0, 1.0]]