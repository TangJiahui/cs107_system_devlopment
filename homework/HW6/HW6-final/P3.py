from random import sample
from time import time
from P2 import *
import heapq as hq

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError


class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)

    def put(self, val):
        if len(self) == self.max_size:
            raise IndexError("Max Size of Priority Queue is Reached!")
        self.elements.append(val)

    def get(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        removed_item = self.peek()
        self.elements.remove(removed_item)
        return removed_item

    def peek(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return min(self.elements)


class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.heap = MinHeap(self.elements)

    def put(self, val):
        if len(self) == self.max_size:
            raise IndexError("Max Size of Priority Queue is Reached!")
        self.heap.heappush(val)

    def get(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return self.heap.heappop()

    def peek(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return self.heap.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.heapq = self.elements
        hq.heapify(self.heapq)

    def put(self, val):
        if len(self) == self.max_size:
            raise IndexError("Max Size of Priority Queue is Reached!")
        hq.heappush(self.heapq, val)

    def get(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return hq.heappop(self.heapq)

    def peek(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return self.heapq[0]


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged

def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists

def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end - start
        elapsed.append(timeaccum / n_average)
    return elapsed


# Q1
# q = NaivePriorityQueue(2)
# q.put(1)
# q.put(2)
# print(q.peek())
# print(q.get())
# print(q.get())
# print(q.elements)
# print(q.get())

# Q2
# q = HeapPriorityQueue(5)
# q.put(1)
# q.put(2)
# q.put(-1)
# q.put(-3)
# q.put(5)
# print(q.peek())
# print(q.get())
# print(q.get())
# print(q.elements)
# print(q.get())

# q = PythonHeapPriorityQueue(5)
# q.put(1)
# q.put(2)
# q.put(-1)
# q.put(-3)
# q.put(5)
# print(q.peek())
# print(q.get())
# print(q.get())
# print(q.heapq)
# print(q.get())