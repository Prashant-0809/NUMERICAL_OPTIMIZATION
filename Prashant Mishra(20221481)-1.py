"""
Name- Prashant Mishra
Examination rollno.-22020570051
Collge rollno.- 20221481
Course- B.Sc.(H) Computer science
"""
import numpy as np
from scipy.optimize import minimize_scalar

# Define your objective function here
def objective_function(x):
    return 2 * x**2 - x + 1  # Example function: f(x) = 2 * x**2 - x + 1

def line_search_method(initial_guess, search_direction):
    
    # Define the objective function to be minimized along the search direction
    def objective_along_direction(alpha):
        x = initial_guess + alpha * search_direction
        return objective_function(x)

    # Perform a line search to find the optimal step size (alpha)
    result = minimize_scalar(objective_along_direction)
    optimal_alpha = result.x

    # Calculate the optimal solution
    optimal_solution = initial_guess + optimal_alpha * search_direction

    return optimal_solution, result.fun

# Usage: 
initial_guess = np.array([0.0])  # Initial guess for the optimization
search_direction = np.array([1.0])  # Search direction

optimal_solution, optimal_value = line_search_method(initial_guess, search_direction)

print("Optimal Solution:", optimal_solution)
print("Optimal Value:", optimal_value)
