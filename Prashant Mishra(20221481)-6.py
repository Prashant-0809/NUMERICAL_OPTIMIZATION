"""
Name- Prashant Mishra
College Rollno- 20221481
Course- B.sc.(H)Computer Science
"""
from scipy.optimize import minimize

# Objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example: minimize x^2 + y^2

# Constraint function
def constraint_function(x):
    return x[0] + x[1] - 1  # Example: constraint x + y = 1

# Initial guess
initial_guess = [0, 0]

# Define the constraint
constraint = {'type': 'eq', 'fun': constraint_function}

# Solve the optimization problem
result = minimize(objective_function, initial_guess, constraints=constraint)

# Print the result
print("Optimal solution:", result.x)
print("Optimal value of the objective function:", result.fun)
