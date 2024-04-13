from math import sqrt
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Finds the distance between two coordinates, with X and Y columns
def distance(coor1: pd.DataFrame, row: pd.DataFrame):
    inner_product = 0

    for col in ["X", "Y"]:
        inner_product += (coor1[col] - row[col])**2

    return sqrt(inner_product)


def generate_knn_regression(k, data: pd.DataFrame):
    knn_data = pd.DataFrame({"X": [], "Y": []})

    for i in range(len(data)):
        knn_data.loc[len(knn_data)] = get_k_nearest_neighbors_point(k, i, data)

    return knn_data.sort_values(by="X")


def get_k_nearest_neighbors_point(k: int, coor_index: int, data: pd.DataFrame):
    current_coor = data.iloc[coor_index]

    new_data = data
    new_data = new_data.drop(coor_index)

    new_data["distance"] = new_data.apply(
        lambda row: distance(current_coor, row), axis="columns")

    new_data = new_data.sort_values(by="distance")
    new_data = new_data.head(k)

    k_coordinate = {"X": new_data["X"].mean(), "Y": new_data["Y"].mean()}

    return k_coordinate


def main():
    data = pd.read_csv("nonlin_df.csv", index_col=0)
    plt.scatter(data["X"], data["Y"])

    k_values = [4, 8, 16]

    for k in k_values:
        knn_data = generate_knn_regression(k, data)
        plt.plot(knn_data["X"], knn_data["Y"], label=f"k = {k}")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
