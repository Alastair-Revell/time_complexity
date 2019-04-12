import random as rn
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import time

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    start_time = time.process_time()
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    total_time = time.process_time() - start_time
    time_list.append(total_time)
    return _quicksort(array, begin, end)

list_size = list(range(500, 10001, 500))
time_list = []

def random_lists(size):
    rnd_list = rn.sample(range(1, size+1), size)
    return rnd_list
#
timing_lists = [random_lists(i) for i in list_size]
[quicksort(i) for i in timing_lists]

#Plotting graph
#
sns.set_style("darkgrid")
new_time_list = np.cumsum(time_list)
plt.plot(list_size, new_time_list, marker='o')
plt.xlabel('List Size')
plt.ylabel('CPU Time')
plt.title('A plot examining Quick Sort Time Efficieny with varying List Sizes')
plt.savefig('quicksort.png')
