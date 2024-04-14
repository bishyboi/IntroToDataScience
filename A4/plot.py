import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame([[0, 0], [1, 1], [2, 0]], columns=['x', 'y'])
sns.set_theme()
fig, ax = plt.subplots()
sns.lineplot(x=df['x'], y=df['y'], ax=ax)

plt.axvspan(0, 2, color = "lightgray", alpha = 0.5)
plt.show()