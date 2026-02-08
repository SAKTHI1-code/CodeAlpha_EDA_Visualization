import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset.csv")

# Display first few rows
print(data.head())

# Dataset information
print(data.info())

# Statistical summary
print(data.describe())

# Check missing values
print(data.isnull().sum())

# Histogram
data.hist(figsize=(8,6))
plt.show()
