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

def random_list(size):
    
#Visualisation of BubbleSort
#Matplotlib / pygame?
