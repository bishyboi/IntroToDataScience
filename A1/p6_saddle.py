from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

bound = 15
detail = 0.05

theta_0 = np.arange(-bound,bound, detail)
theta_1 = np.arange(-bound, bound, detail)

theta_0, theta_1 = np.meshgrid(theta_0, theta_1)

z = theta_0**2 - theta_1**2

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(theta_0, theta_1, z, cmap = "viridis")

# Add labels and title
ax.set_xlabel('Theta Nought')
ax.set_ylabel('Theta One')
ax.set_zlabel('g(theta_0, theta_1)')
ax.set_title('Surface Plot')

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()