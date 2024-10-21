import matplotlib.pyplot as plt
import numpy as np

# Set style for charts
plt.style.use('Solarize_Light2')
print(plt.style.available)

# Create sample set of data
# x is for independent value --> ie) time
x_vals = np.linspace(0, 10,100)

# LINE PLOTS are good when graphing FUNCTIONS 
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# Show figure in IDE
# plt.show()

# Save figure as PNG in current directory
plt.savefig('lineplot.png')

# Alternatively, set up a FIGURE OBJECT for the plot
fig = plt.figure()
ax = plt.axes()

# Plot a function on the Axes object instance
ax.plot(x_vals, 2*(x_vals), color='pink')

fig.savefig('lineplot2.png')