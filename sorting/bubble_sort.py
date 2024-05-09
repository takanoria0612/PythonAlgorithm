# sorting/bubble_sort.py
"""
Bubble Sort Algorithm
"""

def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
        arr (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted array:", bubble_sort(sample_array))
