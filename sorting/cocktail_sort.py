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
        swapped = True

        if not swapped:
            break

        swapped = True
        ## 左から右にソート
        ## 実装
        swapped = True

