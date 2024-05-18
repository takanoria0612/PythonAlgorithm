import pytest
from your_module import cocktail_sort

def test_empty_list():
    assert cocktail_sort([]) == []

## def test_single_element_list():
    ## assert cocktail_sort([1]) == [1]

## def test_sorted_list():
    ## assert cocktail_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

## def test_reverse_list():
    ## assert cocktail_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

## def test_random_list():
    ## assert cocktail_sort([3, 2, 5, 1, 4]) == [1, 2, 3, 4, 5]
