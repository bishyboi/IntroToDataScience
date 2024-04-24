import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example system with linearly dependent equations
A = np.array([[1, 2, 3],
              [10, 4, 6],
              [3, 6, 30],
              [6, 4, 3]])

b = np.array([6, 12, 18])

# Calculate the least squares solution
x = np.linalg.lstsq(A, b, rcond=None)[0]

# Plot the equations and the solution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the equations as planes
for i in range(len(b)):
    xx, yy = np.meshgrid(range(-5, 6), range(-5, 6))
    zz = (b[i] - A[i, 0]*xx - A[i, 1]*yy) / A[i, 2]
    ax.plot_surface(xx, yy, zz, alpha=0.2, label=f'Equation {i+1}')

# Plot the solution point
ax.scatter(x[0], x[1], x[2], color='red', s=100, label='Solution')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.title('Visualization of Overdetermined System with Linearly Dependent Equations')
plt.show()
