import matplotlib.pyplot as plt

x_values = list(range(-1000, 1000))
y_values = [(2*x**2 + 3*x + 1) for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
  edgecolor='none', s=10)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([-1000, 1100, 0, 1100000])

plt.show()