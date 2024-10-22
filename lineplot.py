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
plt.close() # close old plot before making new one

# Alternatively, set up a FIGURE OBJECT for the plot
fig = plt.figure()
ax = plt.axes()

# Plot a function on the Axes object instance
ax.plot(x_vals, 2*(x_vals), color='pink')
ax.plot(x_vals, 3*(x_vals), linestyle= 'dashed')
ax.plot(x_vals, 4*(x_vals), linestyle= 'dashdot')
ax.plot(x_vals, 5*(x_vals), linestyle= 'dotted')

# You can use shortcuts to define color & style
ax.plot(x_vals, 1.5*(x_vals), ':m')

fig.savefig('lineplot2.png')
plt.close()

# Demo on custumization
plt.plot(x_vals, np.sin(x_vals), '--m', label = 'sin(x)')
plt.xlim(-1,11)
plt.ylim(-1.5,1.5)
# Set axis to tight to fit your plot better
plt.axis('tight')
# other options: equal
# Add titles / labels
plt.title('A Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Add legends

plt.legend()
plt.savefig('lineplot3.png')
plt.close()