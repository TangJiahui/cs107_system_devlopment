# class for Toy AD Implementation¶
class AutoDiffToy():
    def __init__(self, val, der = 1):
        self.val = val
        self.der = der

    def __add__(self, other):
        try:
            val =  self.val + other.val
            der = self.der + other.der
        except AttributeError: # real number
            val = self.val + other
            der = self.der
        return AutoDiffToy(val, der)

    def __mul__(self, other):
        try:
            val = self.val * other.val
            der = self.val * other.der + self.der * other.val
        except AttributeError: # real number
            val = self.val * other
            der = self.der * other
        return AutoDiffToy(val, der)

    # for operand not supported due to type
    def __radd__ (self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

# Use case
a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)
alpha = 2.0
beta = 3.0

# test for real number
f_lst = [alpha * x + beta, x * alpha + beta, beta + alpha * x, beta + x * alpha]

for f in f_lst:
    print(f.val, f.der)
#7.0 2.0

# test for two AutoDiff instances
f_obj_lst = [x * x, x * x + x, x + x * x]
for f in f_obj_lst:
    print(f.val, f.der)
# 4.0 4.0
# 6.0 5.0
# 6.0 5.0
