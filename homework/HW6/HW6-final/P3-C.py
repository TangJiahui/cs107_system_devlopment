from P3 import *
import matplotlib.pyplot as plt

ns_lst = [10, 20, 50, 100, 200, 500]
naive_time = timeit(pqclass=NaivePriorityQueue)
heap_time = timeit(pqclass=HeapPriorityQueue)
py_heap_time = timeit(pqclass=PythonHeapPriorityQueue)

## plotting
plt.figure(figsize=(10,7))
plt.plot(ns_lst, naive_time, label = "NaivePriorityQueue")
plt.plot(ns_lst, heap_time, label = "HeapPriorityQueue")
plt.plot(ns_lst, py_heap_time, label = "PythonHeapPriorityQueue")
plt.xlabel("Number of Lists Merged ")
plt.ylabel("Elapsed time in seconds")
plt.title("Performance Comparison of three priority queue implementations")
plt.legend()
plt.show()