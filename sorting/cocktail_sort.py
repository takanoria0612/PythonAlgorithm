from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
    if len(numbers) == 0:
        return numbers
    
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        ## 右から左にソート
        ## 実装
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = True
        end -= 1

        ## 左から右にソート
        for i in range(end -1, start-1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers

