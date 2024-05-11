from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    """
    バブルソートアルゴリズムを使用して整数のリストをソートします。

    引数:
    numbers : List[int]
        ソートされる整数のリスト。

    戻り値:
    List[int]
        ソートされた整数のリスト。
    """
    # リストの各要素に対してループ処理
    for i in range(len(numbers)):
        # バブルソートのパスを実行し、最大の未ソート要素を正しい位置に移動
        for j in range(len(numbers)-1-i):
            # 隣接する要素を比較し、順序が間違っていれば交換
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    import random 
    # 0から100までのランダムな整数で構成されるサンプル配列を10個生成
    sample_array = [random.randint(0, 100) for _ in range(10)]
    print("未ソートの配列:", sample_array)
    print("ソート済みの配列:", bubble_sort(sample_array))

