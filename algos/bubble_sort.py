import random as rn
import time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tqdm import tqdm

def bubbleSort(arr):
    start_time = time.process_time()
    n = len(arr)
    for i in tqdm(range(n)):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    total_time = time.process_time() - start_time
    time_list.append(total_time)
    return arr

list_size = list(range(500, 10001, 500))
time_list = []

def random_lists(size):
    rnd_list = rn.sample(range(1, size+1), size)
    return rnd_list

timing_lists = [random_lists(i) for i in list_size]
[bubbleSort(i) for i in timing_lists]



#Plotting graph

sns.set_style("darkgrid")
new_time_list = np.cumsum(time_list)
plt.plot(list_size, new_time_list, marker='o')
plt.xlabel('List Size')
plt.ylabel('CPU Time')
plt.title('A plot examnining Bubble Sort Time Efficieny with varying List Sizes')
plt.savefig('bubble1.png')
