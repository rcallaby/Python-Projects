import pandas as pd
import matplotlib.pyplot as plt

# Load a dataset (Iris dataset from UCI Machine Learning Repository)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data = pd.read_csv(url, header=None, names=column_names)

# Print first 5 rows of the dataset
print(data.head())

# Calculate mean, median, and standard deviation of each column
print("Mean:\n", data.mean())
print("Median:\n", data.median())
print("Standard deviation:\n", data.std())

# Create a scatter plot of sepal length vs sepal width
plt.scatter(data['sepal_length'], data['sepal_width'])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
