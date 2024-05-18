import pytest
from typing import List
from sorting.bubble_sort import bubble_sort 

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_single_element():
    assert bubble_sort([1]) == [1]

def test_bubble_sort_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_duplicates():
    assert bubble_sort([3, 1, 2, 3, 3]) == [1, 2, 3, 3, 3]

if __name__ == "__main__":
    pytest.main()
