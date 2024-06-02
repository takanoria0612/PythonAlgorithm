def quicksort(array):
    # ベースケース: 配列の長さが1未満の場合、そのまま返す
    if len(array) < 2:
        return array
    else:
        # ピボットを配列の最初の要素に設定
        pivot = array[0]
        # ピボット以下の要素を集めたリストを作成
        less = [i for i in array[1:] if i <= pivot]
        # ピボットより大きい要素を集めたリストを作成
        greater = [i for i in array[1:] if i > pivot]
        # 再帰的にクイックソートを呼び出し、統合して返す
        return quicksort(less) + [pivot] + quicksort(greater)

# ソートされた配列を表示する
print(quicksort([10, 5, 2, 3]))
