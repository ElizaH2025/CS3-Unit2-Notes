import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T # T transposes the data --> switch r & c

plt.style.use('bmh')

# Generate data points
rng = np.random.default_rng(0)
x = rng.normal(size=100)
y = rng.normal(size=100)
colors = rng.random(100)
sizes = 1000 * rng.random(100)
 
# Scatterplot function
# alpha sets the opacity of the point
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
plt.colorbar() # show color scale

# Save figure
plt.savefig('scatterplot.png')
plt.close()

# Scatterplot from iris data
plt.scatter(features[0],features[1], alpha=0.4, s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.colorbar()
plt.savefig('iris-scatter.png')

# 4 different properties observered
# 1)length = x axis
# 2) width = y axis
# 3) dot size = petal width
# 4) color = species