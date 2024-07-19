import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/DATA-ASSESSMENT - Q3 DATA ANALYSIS.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Basic Statistics
print(df.describe())

# Correlation Matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# Histogram of a numeric column
df['numeric_column'].hist()
plt.title('Histogram of Numeric Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Scatter plot between two numeric columns
plt.scatter(df['numeric_column1'], df['numeric_column2'])
plt.title('Scatter Plot between Numeric Column1 and Numeric Column2')
plt.xlabel('Numeric Column1')
plt.ylabel('Numeric Column2')
plt.show()

# Bar chart of a categorical column
df['categorical_column'].value_counts().plot(kind='bar')
plt.title('Bar Chart of Categorical Column')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
