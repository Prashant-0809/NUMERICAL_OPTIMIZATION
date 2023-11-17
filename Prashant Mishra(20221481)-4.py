"""
Name-Prashant Mishra
Collage Rollno- 20221481
Course- B.Sc.(H) Computer Science
"""
import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Set the initial guess
initial_guess = 0.0

# Use the minimize function from scipy.optimize to find the global minimum
result = minimize(objective_function, initial_guess, method='BFGS')

# Print the result
if result.success:
    print("Global optimal solution found at x =", result.x[0])
    print("Optimal function value =", -result.fun)
else:
    print("Optimization failed:", result.message)
