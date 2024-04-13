import pandas as pd
import sklearn as skl
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("car-data.csv")

print("HEAD:")
print(data.head())

print("INFO:")
print(data.info())

print("\n\nDESCRIBE:")
print(data.describe())
print("\n")

if data.isnull().values.any():
    print("There are missing values\n")
else:
    print("There are no missing values\n")
    
"""
Q1
a)
The numerical attributes are: Year, Selling_Price, Present_Price, Kms_Driven, Owner
The categorical attributes are: Car_Name, Fuel_Type, Seller_Type, Transmission

b)
There are no missing data
"""

numerical_cols = data.select_dtypes(include=np.number).columns.tolist()

for numerical_col in numerical_cols:
    plt.figure()
    sns.histplot(data = data, y = numerical_col)
    plt.savefig(f"car_hist_{numerical_col}.png")
    
