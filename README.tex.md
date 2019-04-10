# Introduction to Time-Complexity of Sorting Algorithms #

## Bubble Sort ##

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent pairs of values until a list is sorted.

On average, the bubble sort has a complexity of $O(n^2)$. In an array of length $n$ there are $n-1$ comparisons. In 'big O' notation, this means that there are $O(n)$ comparisons.

Because there are n elements in the array, iterating over the array has a complexity of $O(n)$.

A $O(n)$ operation over a $O(n)$ sized list leads to a complexity of $O(n) \cdot O(n)$ or $O(n^2)$.

Below is a code block for a Bubble Sort Algorithm

```python
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
```
