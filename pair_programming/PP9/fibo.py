#group members: Gabin Ryu, Jiahui Tang, Qinyi Chen
import reprlib

class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return FibonacciIterator(self.n)
    
    def __repr__(self):
        return 'Fibonacci(%s)' % reprlib.repr(self.n)


class FibonacciIterator:
    def __init__(self,n):
        self.index = 0
        self.prev0 = 0
        self.prev1 = 1
        self.curr = 1
        self.n = n

    # has __next__ and __iter__
    def __next__(self): 
        if self.index < self.n:
            self.curr = self.prev0 + self.prev1
            self.index += 1
            self.prev0 = self.prev1
            self.prev1 = self.curr
            return self.curr
        else:
            raise StopIteration()

    
    def __iter__(self):
        return self


#demo
fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
list(iter(fib)) # Iterate over the iterator and create a list.

fib2 = Fibonacci(13) # Create a Fibonacci iterator called fib that contains 13 terms
list(iter(fib2))