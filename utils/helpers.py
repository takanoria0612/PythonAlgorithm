# utils/helpers.py
"""
Helper functions
"""

def is_sorted(arr):
    """
    Checks if a list is sorted.
    
    Parameters:
        arr (list): List of elements to check.
    
    Returns:
        bool: True if sorted, False otherwise.
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
