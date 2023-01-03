# コードの参考
# https://blog.shibayu36.org/entry/2022/12/29/174816
# https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E3%83%92%E3%83%BC%E3%83%97

# ヒープの計算量
# ヒープを自分で実装してみると、1 つのデータの挿入に O(log⁡N) かかるので、
# ヒープの構築には直感的には O(NlogN)かかると思われる。一方で、厳密に計算すると実際は O(N) の計算量になる。
# https://medium.com/@yasufumy/data-structure-heap-ecfd0989e5be


class MinHeap:
    def __init__(self, data=None):
        self.heap = []
        if data is not None:
            for value in data:
                self.push(value)

    def push(self, item):
        # 末端の葉ノードに追加
        self.heap.append(item)
        # 葉ノードから親ノードに向かって、要素がヒープを満たすように交換していく
        self._siftup()
        return self.heap

    def pop(self):
        value = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        self._siftdown()
        return value

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _siftdown(self):
        index = 0
        # O(log⁡N) の計算量が必要
        while 2 * index + 2 < len(self.heap) - 1:
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            # 子のノードのうち、値が小さい方のノードの index を返す
            child_min_index = (
                left_index
                if self.heap[left_index] < self.heap[right_index]
                else right_index
            )
            if self.heap[child_min_index] < self.heap[index]:
                self._swap(index, child_min_index)
            index = child_min_index

    def _siftup(self):
        index = len(self.heap) - 1
        # O(log⁡N) の計算量が必要
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] > self.heap[index]:
                self._swap(parent, index)
            index = parent


heap = MinHeap([0, 1, 3, 5, 4, 3])
print(heap.heap)
print(heap.pop())
print(heap.heap)
print(heap.pop())
print(heap.heap)
