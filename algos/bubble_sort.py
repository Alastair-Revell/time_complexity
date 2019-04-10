import random as rn

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

alist = list(range(500))
rnd_order= rn.sample(alist, k=500)
bubbleSort(rnd_order)

timings = list(range(5000, 100001, 5000))
lists = []

def random_lists(size):
    alist = list(range(size))
    rnd_list = rn.sample(alist, k=size)
    lists.append(rnd_list)
    return lists

print([random_lists(i) for i in timings])
