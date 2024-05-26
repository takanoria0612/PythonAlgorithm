def sum_of_digits(N: int) -> int:
    """
    Calculate the sum of the digits of a given integer.

    Args:
        N (int): The integer whose digits are to be summed. For example, 1234.

    Returns:
        int: The sum of the digits of the integer. For example, if N is 1234, the return value will be 10 (1 + 2 + 3 + 4).

    Example:
        >>> sum_of_digits(1234)
        10
    """
    return sum(int(digit) for digit in str(N))

def validate(digit_sum: int, A: int, B: int) -> bool:
    """
    Check if a given sum of digits is within a specified range.

    Args:
        digit_sum (int): The sum of digits to validate. For example, 10.
        A (int): The lower bound of the range. For example, 5.
        B (int): The upper bound of the range. For example, 15.

    Returns:
        bool: True if the digit_sum is within the range [A, B], False otherwise.

    Example:
        >>> validate(10, 5, 15)
        True
    """
    return A <= digit_sum <= B

def make_digit_list(N: int) -> list[int]:
    """
    Create a list of integers from 1 to N.

    Args:
        N (int): The upper bound of the list. For example, 10.

    Returns:
        list[int]: A list of integers from 1 to N.

    Example:
        >>> make_digit_list(10)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(range(1, N + 1))

def apply_sum_of_digits(digit_list: list[int]) -> list[int]:
    """
    Apply the sum_of_digits function to each element in a list.

    Args:
        digit_list (list[int]): A list of integers. For example, [123, 456, 789].

    Returns:
        list[int]: A list where each element is the sum of digits of the corresponding integer in the input list.

    Example:
        >>> apply_sum_of_digits([123, 456, 789])
        [6, 15, 24]
    """
    return list(map(sum_of_digits, digit_list))

def filter_digit_list(digit_list: list[int], A: int, B: int) -> list[int]:
    """
    Filter a list of digit sums, returning the indices of elements within a specified range.

    Args:
        digit_list (list[int]): A list of digit sums. For example, [6, 15, 24].
        A (int): The lower bound of the range. For example, 5.
        B (int): The upper bound of the range. For example, 20.

    Returns:
        list[int]: A list of indices where the corresponding digit sum is within the range [A, B].

    Example:
        >>> filter_digit_list([6, 15, 24], 5, 20)
        [0, 1]
    """
    return [i for i, digit_sum in enumerate(digit_list) if validate(digit_sum, A, B)]

def make_digit_list_index(digit_list: list[int], indices: list[int]) -> list[int]:
    """
    Get elements from digit_list at specified indices.

    Args:
        digit_list (list[int]): The original list of integers. For example, [1, 2, 3, 4, 5].
        indices (list[int]): The indices of the elements to retrieve from digit_list.

    Returns:
        list[int]: A list of elements from digit_list at the specified indices.

    Example:
        >>> make_digit_list_index([1, 2, 3, 4, 5], [0, 2, 4])
        [1, 3, 5]
    """
    return [digit_list[i] for i in indices]

def main():
    """
    Main function to execute the script. It reads input, processes the data,
    and prints the results.
    """
    N, A, B = map(int, input().split())

    digit_list = make_digit_list(N)
    print("Original list:", digit_list)

    digit_list2 = apply_sum_of_digits(digit_list)
    print("Sum of digits list:", digit_list2)

    digit_list3 = filter_digit_list(digit_list2, A, B)
    print("Filtered indices:", digit_list3)

    result_list = make_digit_list_index(digit_list, digit_list3)
    print("Filtered values:", result_list)

    total_sum = sum(result_list)
    print("Sum of filtered values:", total_sum)

if __name__ == "__main__":
    main()
