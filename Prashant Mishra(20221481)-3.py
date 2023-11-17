"""
Name-Prashant Mishra
Collge Rollno.-20221481
Course- B.Sc.(H) Computer Science
"""
import numpy as np
from scipy.optimize import approx_fprime, check_grad

# Define the function
def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

# Define the point at which to compute the gradient and Hessian
x0 = np.array([0, 0])

# Compute the gradient numerically
gradient = approx_fprime(x0, f, epsilon=1e-8)

# Compute the Hessian numerically
hessian = np.zeros((len(x0), len(x0)))
for i in range(len(x0)):
    hessian[i, :] = approx_fprime(x0, lambda x: approx_fprime(x, f, epsilon=1e-8)[i], epsilon=1e-8)

# Print the results
print("Gradient:")
print(gradient)

print("\nHessian Matrix:")
print(hessian)
000
