# tests/test_sorting.py
"""
Unit tests for bubble sort
"""

import unittest
from sorting.bubble_sort import bubble_sort
from utils.helpers import is_sorted

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = bubble_sort(arr)
        self.assertTrue(is_sorted(sorted_arr))
    
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(bubble_sort([1]), [1])
    
    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
