def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


class PriorityQueue():
    def __init__(self, arr):
        self.list = []
        for num in arr:
            self.insert(num)

    def heapify_up(self):
        index = len(self.list) - 1
        # 親のindexは、(index - 1) // 2
        # 親が小さくなるように入れ替えを繰り返す
        while index != 0 and self.list[index] < self.list[(index - 1) // 2]:
            self.list = swap(self.list, index, (index - 1)//2)
            index = (index-1)//2

    def insert(self, item):
        self.list.append(item)
        self.heapify_up()

    def percolate_down(self):
        if len(self.list) == 2:
            if self.list[0] > self.list[1]:
                self.list = swap(self.list, 0, 1)
        # 上から入れ替えをしていく
        index = 0
        while (2*index + 2 <= len(self.list)-1):
            child_left_index = 2*index + 1
            child_right_index = 2*index + 2
            child_left = self.list[child_left_index]
            child_right = self.list[child_right_index]
            if self.list[index] > min(child_left, child_right):
                if child_left < child_right:
                    self.list = swap(self.list, index, child_left_index)
                    index = child_left_index
                else:
                    self.list = swap(self.list, index, child_right_index)
                    index = child_right_index

    def pop_min(self):
        if len(self.list) == 1:
            return self.list[0]

        min_val = self.list[0]
        # 最後の要素を先頭に持ってくる
        self.list[0] = self.list.pop(-1)
        self.percolate_down()
        return min_val
