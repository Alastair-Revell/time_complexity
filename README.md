# Introduction to Time-Complexity of Sorting Algorithms #

## Bubble Sort ##

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent pairs of values until a list is sorted.

On average, the bubble sort has a complexity of <img src="/tex/3987120c67ed5a9162aa9841b531c3a9.svg?invert_in_darkmode&sanitize=true" align=middle width=43.02219404999999pt height=26.76175259999998pt/>. In an array of length <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> there are <img src="/tex/efcf8d472ecdd2ea56d727b5746100e3.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/> comparisons. In 'big O' notation, this means that there are <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/> comparisons.

Because there are n elements in the array, iterating over the array has a complexity of <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/>.

A <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/> operation over a <img src="/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/> sized list leads to a complexity of <img src="/tex/174e1ae4eb9b0e6d211f792d24f43358.svg?invert_in_darkmode&sanitize=true" align=middle width=83.16745139999999pt height=24.65753399999998pt/> or <img src="/tex/3987120c67ed5a9162aa9841b531c3a9.svg?invert_in_darkmode&sanitize=true" align=middle width=43.02219404999999pt height=26.76175259999998pt/>.

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

Below is a graph of the process time against list size:

<img src="/time_graphs/bubble.png">

### Optimising Bubble Sort ###

It is possible to optimise the bubble sort algorithm after you note that the n-th pass places the n-th elemennt in the correct position. Thus we can avoid looking at the <img src="/tex/efcf8d472ecdd2ea56d727b5746100e3.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/> element on the <img src="/tex/3f18d8f60c110e865571bba5ba67dcc6.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/> pass. In code, we can redefine <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> as <img src="/tex/efcf8d472ecdd2ea56d727b5746100e3.svg?invert_in_darkmode&sanitize=true" align=middle width=38.17727759999999pt height=21.18721440000001pt/> in each loop.

This is more clear after watching the GIF below, after the first pass, 8 is in the correct position and thus does not need to be sorted again.

#### Bubble Sort Gif ####

<img src="time_graphs/Bubble-sort-example-300px.gif" width="500" height="300" />

This leads to the algorithm being almost twice as fast!

<img src="/time_graphs/bubble_optimized.png">

## Merge Sort ##

Merge Sort is more conceptually complex than a bubble sort.

An unsorted list is divided into sublists of 1 element. These sublists are then repeatedly sorted and merged until there is only one sublist remaining. This sublist will be the sorted list.

As above, a gif is a nice way to visualise this:

<img src="time_graphs/Merge-sort-example-300px.gif">
<span style="font-size:2px">Source: Swfung8 [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)]<span>

## Quick Sort ##
The times for quick sort:


<img src="time_graphs/quicksort.png">
