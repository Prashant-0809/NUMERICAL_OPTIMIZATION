"""
Name- Prashant Mishra
Examination rollno.-22020570051
Collge rollno.-20221481
Course- B.Sc.(H) Computer science
"""
import pulp as p
import matplotlib.pyplot as plt
import numpy as np

# Define the Linear Programming Problem
lp_problem = p.LpProblem("Maximize_Profit", p.LpMaximize)

# Define decision variables
x = p.LpVariable("x", lowBound=0)  # x >= 0
y = p.LpVariable("y", lowBound=0)  # y >= 0

# Objective function
lp_problem += 3 * x + 2 * y, "Z"

# Constraints
lp_problem += x + y <= 4
lp_problem += 2 * x + y <= 7

# Solve the LP problem
lp_problem.solve()

# Print the results
print("Status:", p.LpStatus[lp_problem.status])
print("x =", p.value(x))
print("y =", p.value(y))
print("Objective =", p.value(lp_problem.objective))

# Plot the feasible region
x_vals = np.linspace(0, 5, 100)
y1 = 4 - x_vals  # x + y <= 4
y2 = 7 - 2 * x_vals  # 2x + y <= 7

plt.plot(x_vals, y1, label=r'$x + y \leq 4$')
plt.plot(x_vals, y2, label=r'$2x + y \leq 7$')
plt.fill_between(x_vals, 0, y1, where=(y1 >= 0), color='gray', alpha=0.3)
plt.fill_between(x_vals, 0, y2, where=(y2 >= 0), color='gray', alpha=0.3)

# Highlight the optimal point
plt.scatter(p.value(x), p.value(y), color='red', label='Optimal Point')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Feasible Region')
plt.legend()
plt.grid(True)
plt.show()
