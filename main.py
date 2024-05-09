# main.py
"""
Main script to execute bubble sort
"""

from sorting.bubble_sort import bubble_sort
from utils.helpers import is_sorted

def main():
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", sample_array)
    sorted_array = bubble_sort(sample_array)
    print("Sorted array:", sorted_array)
    print("Is sorted:", is_sorted(sorted_array))

if __name__ == "__main__":
    main()
