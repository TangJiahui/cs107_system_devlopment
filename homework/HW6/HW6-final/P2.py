from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        if idx >= self.size:
            return
        # bubbling down by checking with left and right child, find the min/max to swap
        left_idx, right_idx= idx*2+1, idx*2+2
        min_or_max_idx = idx

        for i in [left_idx, right_idx]:
            if i >= self.size:
                continue
            if self.compare(self.elements[i], self.elements[min_or_max_idx]):
                min_or_max_idx = i
        # if min_or_max is updated, swap
        if min_or_max_idx != idx:
            self.swap(idx, min_or_max_idx)
            self.heapify(min_or_max_idx)


    def build_heap(self) -> None:
        # from the last element to very first, heapify by bubbling down
        for i in range(self.size-1, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        # inner function for bubbling up
        def _bubbleup(idx):
            if idx == 0:
                return
            parent_idx = self.parent(idx)
            if self.compare(self.elements[idx], self.elements[parent_idx]):
                self.swap(parent_idx, idx)
                _bubbleup(parent_idx)

        # heap push by adding key to rightmost position, and bubble up
        self.elements.append(key)
        self.size += 1
        _bubbleup(self.size-1)

    def heappop(self) -> int:
        if self.size == 0:
            raise IndexError()
        removed_element = self.elements[0]
        # move the last element to root
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        self.size -= 1
        # bubble down by calling heapify
        self.heapify(0)
        return removed_element


class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        # a: child, b: parent, return true if violates minheap property
        return a < b

class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a > b



# h = MinHeap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
# print(h)
#
# mn = MinHeap([1,2,3,4,5])
# mx = MaxHeap([1,2,3,4,5])
#
# mn.heappush(3)
# mn.heappush(4)
# mn.heappush(1.5)
# mn.heappush(2)
#
# mx.heappop()
# mx.heappop()
# print(mn)
# mn.heappop()
# print(mn)
# mn.heappop()
# print(mn)
# print(mx)