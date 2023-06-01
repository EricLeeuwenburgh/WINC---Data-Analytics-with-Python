# Question: Try to find the clusters in a synthetic (artificial) dataset
# Task:     Make a scatterplot with the centroids of the clusters in red and each cluster with its own color. 
#           Try to determine the correct number of clusters for this dataset.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_columns = 75   # Allows to view more columns (default max = 20)

df = pd.read_csv("https://raw.githubusercontent.com/WincAcademy/practice_data/main/data/winc/synthetic/clustered/clustered_data.csv")

print(df)  

## Plotting the data for a 1st-look visualization
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].scatter(df['a'], df['b'])

axs[0].set_xlabel('a')
axs[0].set_ylabel('b')
axs[0].set_title('1st Look at Data')

#------------------------------------------------------------------------------------------------------------------------------------#

## Determine the optimal number of clusters by using the elbow method:
features = df[['a', 'b']]

# Sum of squared distances for different values of k
sse = []
k_range = range(1, 10)                          # Try different values of k
for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=10)    # N-init suppresses a warning given
    kmeans.fit(features)
    sse.append(kmeans.inertia_)                 # Inertia_ gives the sum of squared distances

axs[1].plot(k_range, sse)
axs[1].set_xlabel('Number of Clusters (k)')
axs[1].set_ylabel('Sum of Squared Distances')
axs[1].set_title('Elbow Curve')

print("According the 'Elbow Curve' the best value for 'k' = 5")

#------------------------------------------------------------------------------------------------------------------------------------#

## K-means clustering with known number for 'K'
k = 5
kmeans = KMeans(n_clusters=k)
kmeans.fit(features)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Scatterplot with results
axs[2].scatter(features['a'], features['b'], c=labels, cmap='viridis')
axs[2].scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')

axs[2].set_xlabel('a')
axs[2].set_ylabel('b')
axs[2].set_title('K-Means Clustering')

plt.tight_layout()
plt.show()