import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='ticks', palette='pastel')
# style: darkgrid, whitegrid, dark, white, ticks
# palette: deep, muted, bright, pastel, dark, colorbind

# Matplotlib histogram
# histograms show distribution of values
data= np.random.multivariate_normal([0,0],[[5,2], [2,2]], size=2000)
data= pd.DataFrame(data, columns=['x','y'])
for col in 'xy':
    plt.hist(data[col], density= True, alpha=.5)
plt.savefig('hist*.png', bbox_inches='tight')
plt.close()

# KDE (kernel density estumation) give a SMOOTH estimate of distribution of values
sns.set_theme(style='dark', palette='bright')
sns.kdeplot(data=data, fill=True)
plt.savefig('sns-kdeplot.png', bbox_inches='tight')
plt.close()

# Load in built-in dataset
iris=sns.load_dataset('iris')
print(iris.head()) # data frame

# Pair Plot allows us to visualize multi-dimensional data
sns.pairplot(iris, hue='species', height=2.5)
plt.savefig('sns-pairplot.png', bbox_inches='tight')
plt.close()