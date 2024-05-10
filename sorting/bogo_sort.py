from random import shuffle

# Function to check if a list is sorted
def is_sorted(numbers):
    # Check if each element is less than or equal to the next element
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

# Bogo Sort function
def bogo_sort(numbers):
    # Shuffle the list until it is sorted
    while not is_sorted(numbers):
        shuffle(numbers)
    return numbers

# Main block to execute the bogo_sort function
if __name__ == "__main__":
    # Test the bogo_sort function with a sample list
    print(bogo_sort([1, 5, 8, 4, 2, 6, 3, 7]))
