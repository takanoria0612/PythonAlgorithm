# Atcoder ABC083B の問題を分割してリフレームして解く

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

## リファクタリング

流石に以上のコードだと汚すぎるので、lambda をふんだんに活用し、可読性の高いコードにリファクタリングした。

### リファクタリングの過程

#### `sum_of_digits`関数のリファクタリング

元の`sum_of_digits`関数は次のようになっている：

```python
def sum_of_digits(N: int) -> int:
    digit_sum = 0
    while N > 0:
        digit_sum += N % 10
        N //= 10
    return digit_sum
```

この関数は、整数 N の各桁の和を計算するものである。これを関数型プログラミングの原則に従って、よりシンプルで宣言的なスタイルにリファクタリングする。

```python
def sum_of_digits(N: int) -> int:
    """
    整数の各桁の和を計算する関数である。

    Args:
        N (int): 桁の和を計算する整数。例：1234

    Returns:
        int: 整数の桁の和。例：Nが1234なら、戻り値は10 (1 + 2 + 3 + 4) である。

    Example:
        >>> sum_of_digits(1234)
        10
    """
    return sum(int(digit) for digit in str(N))
```

**改善点**：

- `while`ループを使用せず、リスト内包表記と組み込み関数`sum`を用いることで、より簡潔かつ読みやすくなっている。
- この関数は純粋であり、副作用を持たない。

#### `validate`関数のリファクタリング

元の`validate`関数は次のようになっている：

```python
def validate(digit_sum: int, A: int, B: int) -> bool:
    return A <= digit_sum <= B
```

この関数はすでにシンプルかつ機能的であるため、大きな変更は必要ない。しかし、ドキュメントを追加する。

```python
def validate(digit_sum: int, A: int, B: int) -> bool:
    """
    与えられた桁の和が指定された範囲内にあるかどうかをチェックする関数である。

    Args:
        digit_sum (int): 検証する桁の和。例：10。
        A (int): 範囲の下限。例：5。
        B (int): 範囲の上限。例：15。

    Returns:
        bool: digit_sumが範囲[A, B]内にあればTrueを、そうでなければFalseを返す。

    Example:
        >>> validate(10, 5, 15)
        True
    """
    return A <= digit_sum <= B
```

**改善点**：

- ドキュメントを追加し、関数の目的と使用方法を明確にした。

#### `make_digit_list`関数のリファクタリング

元の`make_digit_list`関数は次のようになっている：

```python
def make_digit_list(N: int) -> list[int]:
    return [i for i in range(1, N + 1)]
```

リスト内包表記を使用しているが、`range`関数を直接リスト化する方が簡潔である。

```python
def make_digit_list(N: int) -> list[int]:
    """
    1からNまでの整数リストを作成する関数である。

    Args:
        N (int): リストの上限。例：10。

    Returns:
        list[int]: 1からNまでの整数リスト。

    Example:
        >>> make_digit_list(10)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    return list(range(1, N + 1))
```

**改善点**：

- `range`関数を直接リスト化することで、コードがさらに簡潔になっている。

#### `apply_sum_of_digits`関数のリファクタリング

元の`apply_sum_of_digits`関数は次のようになっている：

```python
def apply_sum_of_digits(digit_list: list[int]) -> list[int]:
    return [sum_of_digits(i) for i in digit_list]
```

リスト内包表記を使用しているが、関数型プログラミングの原則に従い`map`関数を使用する。

```python
def apply_sum_of_digits(digit_list: list[int]) -> list[int]:
    """
    リストの各要素にsum_of_digits関数を適用する関数である。

    Args:
        digit_list (list[int]): 整数のリスト。例： [123, 456, 789]。

    Returns:
        list[int]: 各要素が元のリストの対応する整数の桁の和であるリスト。

    Example:
        >>> apply_sum_of_digits([123, 456, 789])
        [6, 15, 24]
    """
    return list(map(sum_of_digits, digit_list))
```

**改善点**：

- `map`関数を使用することで、関数の適用がより宣言的かつ機能的になっている。

#### `filter_digit_list`関数のリファクタリング

元の`filter_digit_list`関数は次のようになっている：

```python
def filter_digit_list(digit_list: list[int], A: int, B: int) -> list[int]:
    return [i for i in range(len(digit_list)) if validate(digit_list[i], A, B)]
```

リスト内包表記と`enumerate`を組み合わせることで、より読みやすくする。

```python
def filter_digit_list(digit_list: list[int], A: int, B: int) -> list[int]:
    """
    指定された範囲内にある要素のインデックスを返す関数である。

    Args:
        digit_list (list[int]): 桁の和のリスト。例： [6, 15, 24]。
        A (int): 範囲の下限。例：5。
        B (int): 範囲の上限。例：20。

    Returns:
        list[int]: 範囲[A, B]内にある対応する桁の和の要素のインデックスのリスト。

    Example:
        >>> filter_digit_list([6, 15, 24], 5, 20)
        [0, 1]
    """
    return [i for i, digit_sum in enumerate(digit_list) if validate(digit_sum, A, B)]
```

**改善点**：

- `enumerate`を使用することで、インデックスと要素のペアをより簡潔に扱うことができる。

#### `make_digit_list_index`関数のリファクタリング

元の`make_digit_list_index`関数は次のようになっている：

```python
def make_digit_list_index(digit_list: list[int], indices: list[int]) -> list[int]:
    return [digit_list[i] for i in indices]
```

この関数はすでにシンプルで機能的であるため、大きな変更は必要ない。

```python
def make_digit_list_index(digit_list: list[int], indices: list[int]) -> list[int]:
    """
    指定されたインデックスでdigit_listから要素を取得する関数である。

    Args:
        digit_list (list[int]): 元の整数のリスト。例： [1, 2, 3, 4, 5]。
        indices (list[int]): digit_listから取得する要素のインデックス。例： [0, 2, 4]。

    Returns:
        list[int]: 指定されたインデックスでdigit_listから取得された要素のリスト。

    Example:
        >>> make_digit_list_index([1, 2, 3, 4, 5], [0, 2, 4])
        [1, 3, 5]
    """
    return [digit_list[i] for i in indices]
```

#### `main`関数のリファクタリング

`main`関数は次のようになっている：

```python
def main():
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


```

**改善点**：

- 既存の関数を適切に呼び出し、結果を出力する。
- `sum_of_this_problem`関数を削除し、`sum`関数を直接使用することで冗長性を排除。

以上のリファクタリングにより、コードは関数型プログラミングの原則により適合し、より簡潔で読みやすくなった。これにより、コードの保守性と再利用性が向上した。
