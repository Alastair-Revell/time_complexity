import pytest
from merge_sort import *

def test_one():
    test_list = random_lists(5)
    print(test_list)
    sorted_list = bubbleSort(test_list)
    print(sorted_list)
    assert(sorted_list == [1,2,3,4,5])
