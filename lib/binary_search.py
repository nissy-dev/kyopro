class BinarySearch:
    # x 以上の値を持つ最小の index を返す
    def lower_bound(self, arr, x):
        left = -1
        right = len(arr)
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid
        return right

    # x 以降の値を持つ最小の index を返す
    def upper_bound(self, arr, x):
        left = -1
        right = len(arr)
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        return right
