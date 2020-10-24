import numpy as np
import matplotlib.pyplot as plt

# Part A: Numerical Differentiation Closure
def numerical_diff(f,h):
    def inner(x):
        return (f(x+h) - f(x))/h
    return inner

# Part B:
f = np.log
x = np.linspace(0.2, 0.4, 500)
h = [1e-1, 1e-7, 1e-15]
y_analytical = 1/x
result = {}


for i in h:
    y = numerical_diff(f,i)(x)
    result[i] = y

# Plotting
plt.figure(figsize = (8,5))
plt.plot(x, y_analytical, 'x-', label='Analytical Derivative')
for i in h:
    plt.plot(x, result[i], label='Estimated derivative h = '+str(i))
plt.xlabel("X value")
plt.ylabel("Derivative Value at X")
plt.title("Differentiation Value at X on various h value")
plt.legend()


# Part C:
print("Answer to Q-a: When h value is 1e-7, it most closely approximates the true derivative. \n",
      "When h value is too small: The approximation is jumping around stepwise and not displaying a smooth curve approximation, it amplifies floating point errors in numerical operation such as rounding and division\n",
      "When h value is too large: The approximation is lower than the true value, it doesn't provide a good approximation to the derivative\n")
print("Answer to Q-b: Automatic differentiation avoids the problem of not choosing a good h value. \n"
      "The finite difference approach is quick and easy but suffers from accuracy and stability problems.\n"
      "Symbolic derivatives can be evaluated to machine precision, but can be costly to evaluate.\n"
      "Automatic differentiation (AD) overcomes both of these deficiencies. It is less costly than symbolic differentiation while evaluating derivatives to machine precision.\n"
      "AD uses forward or backward modes to differentiate, via Computational Graph, chain rule and evaluation trace.")

# Show plot
plt.show()
# plt.savefig('P1_fig.png')

