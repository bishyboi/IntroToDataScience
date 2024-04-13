from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv("nonlin_df.csv", index_col=0)

x = data["X"].to_numpy()
y = data["Y"].to_numpy()

# Plotting all data points
plt.scatter(x,y)

# Calculating the terms in the formula
x_mean = np.average(x)
y_mean = np.average(y)

xy_mean = np.average(x*y)
x_squared_mean = np.average(x*x)

# Less calculations to solve theta one first, because rearranging vars shows y_mean - theta_one * x_mean = theta_nought
theta_one = (xy_mean - (x_mean*y_mean)) / (x_squared_mean - x_mean**2)
theta_nought = y_mean - theta_one*x_mean

print(f"Linear function: y = {theta_nought:.2f}+ {theta_one:.2f}x")

# Plotting the linear regression following y = theta_nought + theta_one*x
linear_x = np.linspace(0, 15, 2)
plt.plot(linear_x, theta_nought + theta_one*linear_x, color = "red")

# Plotting y = x^2.5
linear_x = np.linspace(0,15,1000)
plt.plot(linear_x, linear_x**2.5, "magenta")

# Show the plot
plt.show()
