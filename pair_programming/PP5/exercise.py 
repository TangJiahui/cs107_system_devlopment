### PP5

# Coder: Sarah Zeng, Jiahui Tang
# Sharer: Omead Eftekhari
# Listener:

import numpy as np

class Layer():
    def __init__(self, shape, actv):
        # shape : a lst of 2 elements of row and col 
        self.shape = shape
    
        # input = [shape[0], shape[1]], weight = [shape[1],1], bias = [1]
        self.actv = actv
        self.weights = np.random.uniform(0.0, 1.0, self.shape[1]).reshape(self.shape[1],-1)
        self.bias = np.random.uniform(0.0,1.0,self.shape[1]).reshape(1,-1)
    
    def forward(self, inputs):
       return self.actv(np.dot(inputs, self.weights) + self.bias)
       
    def __str__(self):
        class_name = type(self).__name__
        return "created {0}".format(class_name)

    def __repr__(self):
        class_name = type(self).__name__
        return "%s(shape=%r, actv func=%r)" % (class_name, self.shape, self.actv.__name__)
        
    def __len__(self):
        return len(self.shape)
    

## Tests

shape_1 = [3,3]
input_1 = np.random.uniform(0.0, 1.0, 3).reshape(1,-1)
layer1 = Layer(shape_1, np.tanh)
h1 = layer1.forward(input_1)

shape_2 = [6,3]
layer2 = Layer(shape_2, np.tanh)
h2 = layer2.forward(h1)

print(h1)
print(h2)

## Dunder testing

print(str(layer1))
print(str(layer2))

print(repr(layer1))
print(repr(layer2))

print(len(layer1))
print(len(layer2))