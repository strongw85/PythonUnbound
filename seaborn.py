# -*- coding: utf-8 -*-
"""Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HXhUdESE2AKapVxUcm346f7WfbVH8FZ4
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Scatter Plot
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris)
plt.show()

# Line Plot
sns.lineplot(x="petal_length", y="petal_width", data=iris)
plt.show()

# Bar Plot
sns.barplot(x="species", y="sepal_length", data=iris)
plt.show()

# Violin Plot
sns.violinplot(x="species", y="petal_length", data=iris)
plt.show()

"""This code demonstrates how to create a scatter plot, line plot, bar plot, and violin plot using the Seaborn library. Each plot represents different aspects of the iris dataset and provides different ways of visualizing the data."""

import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = sns.load_dataset("iris")

# Customizing color and markers
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris, color="green", marker="D")
plt.show()

# Customizing the style of the plot
sns.set_style("darkgrid")
sns.scatterplot(x="petal_length", y="petal_width", data=iris)
plt.show()

# Customizing the color palette
sns.violinplot(x="species", y="petal_length", data=iris, palette="pastel")
plt.show()

# Customizing plot size
sns.scatterplot(x="petal_length", y="petal_width", data=iris)
plt.gcf().set_size_inches(10, 5)
plt.show()

"""This code demonstrates how to customize the color, markers, style, color palette, and size of a scatter plot in Seaborn using the iris dataset. By using these customization options, users can create plots that effectively communicate insights and meet their specific needs."""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the iris dataset into a pandas dataframe
iris = sns.load_dataset("iris")

# Customize a scatter plot
sns.scatterplot(x="sepal_length", y="sepal_width", data=iris, hue="species", palette="dark")
plt.title("Scatter Plot of Sepal Length vs. Sepal Width")
plt.show()

# Customize a violin plot
sns.violinplot(x="species", y="petal_length", data=iris, inner="stick", palette="pastel")
plt.title("Violin Plot of Petal Length by Species")
plt.show()

# Customize a line plot
sns.lineplot(x="species", y="petal_width", data=iris, sort=False, marker="o", linewidth=2)
plt.title("Line Plot of Petal Width by Species")
plt.show()

# Customize a bar plot
sns.barplot(x="species", y="sepal_length", data=iris, color="green", capsize=0.1)
plt.title("Bar Plot of Sepal Length by Species")
plt.show()