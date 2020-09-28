"""
PP4

Collaborator: 
Jiahui Tang
Yang Xiang
ChunChao Tseng
"""

import numpy as np
import math


## closure
def layer(shape, actv):
    def inner(inputs, weights, bias):
        # inputs @ weights + bias 
        return actv(inputs @ weights + bias)
    return inner


## demo & testing
t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network #1*100

shape1 = [100, 4]
shape2 = [4, 5]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.random.uniform(0.0,1.0,400).reshape(100,-1) #100*4
w2 = np.random.uniform(0.0,1.0,20).reshape(4,-1) #4*5
b1 = np.random.uniform(0.0,1.0,4).reshape(1,-1) #4*1
b2 = np.random.uniform(0.0,1.0,5).reshape(1,-1) #1*5 

# Run through the network
h1 = layer1(t, w1, b1) # First layer #1*4
h2 = layer2(h1, w2, b2) # Last layer
print(h1, h2)