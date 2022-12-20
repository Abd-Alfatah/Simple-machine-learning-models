import multiprocessing
import time
import numpy as np
results=list()
np.random.RandomState(100)
arr=np.random.randint(0,10,size=[2000,5])
data=arr.tolist()
data[:5]
start=time.perf_counter()
def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)
        time.sleep(0.2)

    q.put(-1)
    print('Exiting function')
def howmany_with_in_range2(i,row,minimum,maximum):
    count =0
    for n in row:
        if minimum <= n <=maximum:
            count =count +1
    return (i,count)
def collect_result(result):
    results.append(result)

if __name__ == '__main__':
    print('Now in the main code. Process name is:', __name__)
    numbers = [2, 3, 4, 5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, q))
    p.start()
    import multiprocessing as mp 
    pool = mp.Pool(mp.cpu_count())
    q.put(4)
    for i, row in enumerate(data):
        pool.apply_async(howmany_with_in_range2, args=(i,row, 4, 8), callback=collect_result)
    while True:
        nq = q.get()
        print('Message is:', nq)
        if nq == -1:
            break

    print('Done')
    p.join()
    pool.close()
    pool.join()
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]
    print(results_final[:10])
end=time.perf_counter()
print(end-start)