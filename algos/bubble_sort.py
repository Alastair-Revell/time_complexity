import random as rn
import time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def bubbleSort(arr):
    start_time = time.process_time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        n = n-1
    total_time = time.process_time() - start_time
    time_list.append(total_time)

timings = list(range(5000, 100001, 5000))
lists = []
time_list = []

def random_lists(size):
    rnd_list = rn.sample(range(1, size+1), size)
    lists.append(rnd_list)
    return lists

timing_lists = [random_lists(i) for i in timings]
[bubbleSort(i) for i in timing_lists]
import seaborn as sns

sns.set_style("darkgrid")
new_time_list = np.cumsum(time_list)
plt.plot(timings, new_time_list, marker='o')
plt.xlabel('List Size')
plt.ylabel('CPU Time')
plt.title('A plot examnining Bubble Sort Time Efficieny with varying List Sizes')
plt.savefig('bubble1.png')
