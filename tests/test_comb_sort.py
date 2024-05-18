import pytest
from sorting.comb_sort import comb_sort

def test_empty_list():
    assert comb_sort([]) == []
    comb_sort([1, 2, 3, 4, 5])

def test_single_element_list():
    assert comb_sort([1]) == [1]

def test_sorted_list():
    assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_list():
    assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_random_list():
    assert comb_sort([3, 2, 5, 1, 4]) == [1, 2, 3, 4, 5]


