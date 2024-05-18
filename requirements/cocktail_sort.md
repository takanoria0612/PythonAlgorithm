ここで大切なのは、ゴールはソートをすることではなく、カクテルソートを使ってソートをすることである。
### 要件の理解

#### 入力
- [ ] 整数のリスト `numbers` を受け取る。

#### 出力
- [ ] ソートされた整数のリストを返す。

### 大まかなタスクの分解

1. **リストの長さを取得する。**
    - [ ] リストの長さを変数 `len_numbers` に代入する。

2. **初期設定（変数の初期化）を行う。**
    - [ ] 変数 `swapped` を `True` に初期化する。
    - [ ] 変数 `start` を `0` に初期化する。
    - [ ] 変数 `end` を `len_numbers - 1` に初期化する。

3. **リストの先頭から末尾に向かって比較・交換を行う。**
    - [ ] `start` から `end` までループを行う。
        - [ ] 現在の要素と次の要素を比較する。
        - [ ] 必要に応じて要素を交換し、`swapped` を `True` に設定する。

4. **リストの末尾から先頭に向かって比較・交換を行う。**
    - [ ] `end - 1` から `start` まで逆向きにループを行う。
        - [ ] 現在の要素と次の要素を比較する。
        - [ ] 必要に応じて要素を交換し、`swapped` を `True` に設定する。

5. **両方向でのソートが完了するまで繰り返す。**
    - [ ] `swapped` が `False` になるまでループを続ける。

### 具体的なタスクの分解

1. **リストが空かどうかを確認し、空ならそのまま返す。**
    - [ ] リスト `numbers` が空の場合、`numbers` をそのまま返す。

2. **リストの長さを取得し、必要な変数を初期化する。**
    - [ ] リスト `numbers` の長さを `len_numbers` に代入する。
    - [ ] 変数 `swapped` を `True` に初期化する。
    - [ ] 変数 `start` を `0` に初期化する。
    - [ ] 変数 `end` を `len_numbers - 1` に初期化する。

3. **ソートが必要な場合、先頭から末尾に向かって比較・交換を行う。**
    - [ ] `while swapped:` ループを開始する。
    - [ ] 変数 `swapped` を `False` に設定する。
    - [ ] `for i in range(start, end):` ループを開始する。
        - [ ] `if numbers[i] > numbers[i + 1]:` をチェックする。
            - [ ] `numbers[i]` と `numbers[i + 1]` を交換する。
            - [ ] 変数 `swapped` を `True` に設定する。

4. **リストの末尾から先頭に向かって比較・交換を行う。**
    - [ ] `if not swapped:` ブロックを追加する。
        - [ ] `break` でループを終了する。
    - [ ] 変数 `swapped` を `False` に設定する。
    - [ ] 変数 `end` を `end - 1` に設定する。
    - [ ] `for i in range(end - 1, start - 1, -1):` ループを開始する。
        - [ ] `if numbers[i] > numbers[i + 1]:` をチェックする。
            - [ ] `numbers[i]` と `numbers[i + 1]` を交換する。
            - [ ] 変数 `swapped` を `True` に設定する。

5. **ソートが完了するまでループを続ける。**
    - [ ] 変数 `start` を `start + 1` に設定する。
    - [ ] `while swapped:` ループの終了を確認する。

### 実装ステップ

#### 1. リストが空かどうかを確認し、空ならそのまま返す。
```python
from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
    if len(numbers) == 0:
        return numbers
```

#### 2. リストの長さを取得し、必要な変数を初期化する。
```python
from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
    if len(numbers) == 0:
        return numbers
    
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
```

#### 3. ソートが必要な場合、先頭から末尾に向かって比較・交換を行う。
```python
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
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
```

#### 4. リストの末尾から先頭に向かって比較・交換を行う。
```python
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
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        
        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
```

#### 5. ソートが完了するまでループを続ける。
```python
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
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        
        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        
        start = start + 1
    
    return numbers
```

### テストコード（pytestを使用）

```python
import pytest
from your_module import cocktail_sort

def test_empty_list():
    assert cocktail_sort([]) == []

def test_single_element_list():
    assert cocktail_sort([1]) == [1]

def test_sorted_list():
    assert cocktail_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_list():
    assert cocktail_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_random_list():
    assert cocktail_sort([3, 2, 5, 1, 4]) == [1, 2, 3, 4, 5]
```

このプロセスに従って、TDDを用いたカクテルソートの実装を行うことで、各ステップの実装を確実に行い、すべてのテストケースをパスすることができます。