class BinarySearch:
    # arr の中に x 含まれているか探索
    def is_include(self, arr, x):
        left = -1
        right = len(arr) - 1
        while right-left > 1:
            mid = left + (right-left)//2
            if x == arr[mid]:   # xがちょうど中間にあったとき
                return mid
            elif x < arr[mid]:  # xが左側の配列にあるとき
                right = mid
            else:               # xが右側の配列にあるとき
                left = mid
        if x == arr[right]:
            return right
        return -1

    # x 以上の値を持つ最小の index を返す
    def lower_bound(self, arr, x):
        left = -1
        right = len(arr) - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid
        return right

    # x 以降の値を持つ最小の index を返す
    def upper_bound(self, arr, x):
        left = -1
        right = len(arr) - 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        return right
