from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np

data = pd.read_csv("lin_df.csv", index_col=0)

x = data["X"].to_numpy()
y = data["Y"].to_numpy()

# Calculating the terms in the formula
x_mean = np.average(x)
y_mean = np.average(y)

xy_mean = np.average(x*y)
x_squared_mean = np.average(x*x)
y_squared_mean = np.average(y*y)

bound = 15
detail = 0.05

theta_0 = np.arange(-bound,bound, detail)
theta_1 = np.arange(-bound, bound, detail)

theta_0, theta_1 = np.meshgrid(theta_0, theta_1)

z =( y_squared_mean
    - 2*theta_0*y_mean 
    - 2*theta_1*xy_mean 
    + theta_0**2 
    + 2*theta_0*theta_1*x_mean 
    + (theta_1**2) * (theta_1**2))


min_index = np.unravel_index(np.argmin(z), z.shape)

# Extract the corresponding theta_0 and theta_1 values
min_theta_0 = theta_0[min_index]
min_theta_1 = theta_1[min_index]

# Print the coordinates of the minimum z value
print("Coordinates of the minimum z value:")
print("Theta_0:", min_theta_0)
print("Theta_1:", min_theta_1)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(theta_0, theta_1, z, cmap = "viridis")


# Plot the minimum point as a red dot
ax.scatter(min_theta_0, min_theta_1, np.min(z) , color='red', s=100, label='Minimum')


# Add labels and title
ax.set_xlabel('Theta Nought')
ax.set_ylabel('Theta One')
ax.set_zlabel('h(theta_0, theta_1)')
ax.set_title('Surface Plot')

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.legend()
plt.show()