# Introduction to Time-Complexity of Sorting Algorithms #

## Bubble Sort ##

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent pairs of values until a list is sorted.

On average, the bubble sort has a complexity of $O(n^2)$. In an array of length $n$ there are $n-1$ comparisons. In 'big O' notation, this means that there are $O(n)$ comparisons.

Because there are n elements in the array, iterating over the array has a complexity of $O(n)$.

A $O(n)$ operation over a $O(n)$ sized list leads to a complexity of $O(n) \cdot O(n)$ or $O(n^2)$.

### Bubble Sort Code ###

```python
import random as rn

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

rnd_order= rn.sample(range(1, 501), 500)

bubbleSort(rnd_order)
```

### Bubble Sort Times ###

<img src="/time_graphs/bubble.png">

### Optimising Bubble Sort ###

It is possible to optimise the bubble sort algorithm after you note that the n-th pass places the n-th elemennt in the correct position. Thus we can avoid looking at the $n-1$ element on the $n+1$ pass. In code, we can redefine $n$ as $n-1$ in each loop. This is more clear after watching the GIF below, after the first pass, 8 is in the correct position and thus does not need to be sorted again.

#### Bubble Sort Gif #### 

<img src="time_graphs/Bubble-sort-example-300px.gif" width="500" height="300" />

This leads to the algorithm being almost twice as fast!

<img src="/time_graphs/bubble_optimized.png">
