````markdown
# Atcoder 問題解法プロセス

この md ファイルでは、以下の Atcoder の問題を解いたプロセスを詳述する。問題文は次の通りである。

**問題文**：  
1 以上 N 以下の整数の、10 進数での各桁の和が A 以上 B 以下であるものの総和を求めてください。

提供されたコードをもとに、どのようにして問題を分割し、関数化して解決したかのプロセスを説明する。

## 問題の分割と関数化

まず、問題文を以下のステップに分割して解決することにした。

1. 各整数の桁の和を計算する関数の作成
2. 桁の和が指定範囲内にあるかをチェックする関数の作成
3. 1 から N までの整数リストを生成する関数の作成
4. 各整数の桁の和を求める関数の作成
5. 桁の和が指定範囲内にある整数をフィルタリングする関数の作成
6. フィルタリングされた整数のリストの総和を計算する関数の作成

以下に、各ステップに対応する関数の実装とその説明を示す。

### 1. 各整数の桁の和を計算する関数

```python
def sum_of_digits(N: int) -> int:
    """
    各桁の和を計算する関数。

    Args:
        N (int): 桁の和を計算する整数。例：1234

    Returns:
        int: 桁の和。例：Nが1234なら、1 + 2 + 3 + 4 = 10

    Example:
        >>> sum_of_digits(1234)
        10
    """
    digit_sum = 0
    while N > 0:
        digit_sum += N % 10  # 最後の桁を抽出して加算
        N //= 10             # 最後の桁を削除
    return digit_sum
```
````

この関数は与えられた整数の各桁を分解し、その和を計算する。例えば、1234 を入力とした場合、1 + 2 + 3 + 4 = 10 が返される。

### 2. 桁の和が指定範囲内にあるかをチェックする関数

```python
def validate(digit_sum: int, A: int, B: int) -> bool:
    """
    桁の和が指定範囲内にあるかをチェックする関数。

    Args:
        digit_sum (int): 桁の和。例：10
        A (int): 範囲の下限。例：5
        B (int): 範囲の上限。例：15

    Returns:
        bool: digit_sumが範囲[A, B]内にある場合はTrue、そうでない場合はFalse。

    Example:
        >>> validate(10, 5, 15)
        True
    """
    return A <= digit_sum <= B
```

この関数は、桁の和が指定された範囲内にあるかどうかをチェックする。例えば、桁の和が 10 で、範囲が 5 から 15 であれば、True が返される。

### 3. 1 から N までの整数リストを生成する関数

```python
def make_digit_list(N: int) -> list[int]:
    """
    1からNまでの整数リストを生成する関数。

    Args:
        N (int): リストの上限。例：10

    Returns:
        list[int]: 1からNまでの整数リスト。例：Nが10なら、[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Example:
        >>> make_digit_list(10)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return [i for i in range(1, N + 1)]
```

この関数は、1 から N までの整数を含むリストを生成する。例えば、N が 10 なら、[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]が返される。

### 4. 各整数の桁の和を求める関数

```python
def apply_sum_of_digits(digit_list: list[int]) -> list[int]:
    """
    リスト内の各整数に対してsum_of_digits関数を適用する関数。

    Args:
        digit_list (list[int]): 整数リスト。例：[123, 456, 789]

    Returns:
        list[int]: 各整数の桁の和のリスト。例：入力が[123, 456, 789]なら、[6, 15, 24]

    Example:
        >>> apply_sum_of_digits([123, 456, 789])
        [6, 15, 24]
    """
    return [sum_of_digits(i) for i in digit_list]
```

この関数は、整数リストの各要素に対して`sum_of_digits`関数を適用し、各整数の桁の和を求める。

### 5. 桁の和が指定範囲内にある整数をフィルタリングする関数

```python
def filter_digit_list(digit_list: list[int], A: int, B: int) -> list[int]:
    """
    桁の和が指定範囲内にある整数をフィルタリングする関数。

    Args:
        digit_list (list[int]): 桁の和のリスト。例：[6, 15, 24]
        A (int): 範囲の下限。例：5
        B (int): 範囲の上限。例：20

    Returns:
        list[int]: 範囲内の桁の和を持つ整数のインデックスのリスト。例：入力が[6, 15, 24]、Aが5、Bが20なら、[0, 1]

    Example:
        >>> filter_digit_list([6, 15, 24], 5, 20)
        [0, 1]
    """
    return [i for i in range(len(digit_list)) if validate(digit_list[i], A, B)]
```

この関数は、桁の和が指定範囲内にある整数のインデックスをフィルタリングする。例えば、入力が[6, 15, 24]、範囲が 5 から 20 なら、[0, 1]が返される。

### 6. フィルタリングされた整数のリストの総和を計算する関数

```python
def sum_of_this_problem(num_list: list[int]) -> int:
    """
    整数リストの総和を計算する関数。

    Args:
        num_list (list[int]): 整数リスト。例：[1, 3, 5]

    Returns:
        int: リスト内の整数の総和。例：入力が[1, 3, 5]なら、1 + 3 + 5 = 9

    Example:
        >>> sum_of_this_problem([1, 3, 5])
        9
    """
    return sum(num_list)
```

この関数は、フィルタリングされた整数リストの総和を計算する。例えば、入力が[1, 3, 5]なら、1 + 3 + 5 = 9 が返される。

### メイン関数

```python
def main():
    """
    メイン関数。入力を読み込み、データを処理し、結果を出力する。
    """
    N, A, B = map(int, input().split())

    digit_list = make_digit_list(N)
    print("Original list:", digit_list)

    digit_list2 = apply_sum_of_digits(digit_list)
    print("Sum of digits list:", digit_list2)

    digit_list3 = filter_digit_list(digit_list2, A, B)
    print("Filtered indices:", digit_list3)

    def make_digit_list_index(digit_list: list[int], indices: list[int]) -> list[int]:
        """
        指定されたインデックスの要素を取得する関数。

        Args:
            digit_list (list[int]): 元の整数リスト。例：[1, 2, 3, 4, 5]
            indices (list[int]): インデックスのリスト。例：[0, 2, 4]

        Returns:
            list[int]: インデックスで指定された要素のリスト。例：入力が[1, 2, 3, 4, 5]、インデックスが[0, 2, 4]なら、[1, 3, 5]



        Example:
            >>> make_digit_list_index([1, 2, 3, 4, 5], [0, 2, 4])
            [1, 3, 5]
        """
        return [digit_list[i] for i in indices]

    result_list = make_digit_list_index(digit_list, digit_list3)
    print("Filtered values:", result_list)

    total_sum = sum_of_this_problem(result_list)
    print("Sum of filtered values:", total_sum)

if __name__ == "__main__":
    main()
```

メイン関数は、入力を読み込み、上記の関数を順に呼び出してデータを処理し、結果を出力する。各ステップでリストが生成され、最終的にフィルタリングされた整数の総和が計算される。

このように、問題を細かく分割し、関数化することで、コードの可読性と再利用性を高め、問題を効率的に解決することができた。
