"""
Name- Prashant MIshra
Collage Rollno-20221481
Course- B.Sc.(H) Computer Science
"""
import numpy as np
import matplotlib.pyplot as plt

# Rest of the code remains unchanged


# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Generate x values
x_values = np.linspace(-5, 5, 1000)

# Calculate corresponding y values
y_values = objective_function(x_values)

# Plot the function
plt.plot(x_values, y_values, label='f(x)')

# Find the minimum of the function
min_x = x_values[np.argmin(y_values)]
min_y = objective_function(min_x)

# Mark the minimum point on the plot
plt.scatter(min_x, min_y, color='red', label='Global Minimum')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graphical Representation of f(x)')

# Display the legend
plt.legend()

# Show the plot
plt.show()

# Print the result
print("Global optimal solution found at x =", min_x)
print("Optimal function value =", min_y)
