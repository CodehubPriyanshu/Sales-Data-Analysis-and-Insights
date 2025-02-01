# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO

try:
    import seaborn as sns
except ImportError:
    !pip install seaborn
    import seaborn as sns

# 1. Data Cleaning and Loading
print("1. Data Cleaning and Loading")

# Replace 'sales_data_sample.csv' with the actual file name if different
file_path = './sales_data_sample.csv'  # Ensure the correct path

# Try different encodings
encodings = ['utf-8', 'iso-8859-1', 'cp1252']
for encoding in encodings:
    try:
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path, encoding=encoding)
        print(f"Successfully loaded the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to decode with encoding: {encoding}")
else:
    raise ValueError("Unable to decode the CSV file with any of the attempted encodings.")

# Display basic information about the dataset
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()  # Remove rows with missing values

# Convert date columns to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

print("\nDataset shape after cleaning:", df.shape)

# 2. Exploratory Data Analysis (EDA)
print("\n2. Exploratory Data Analysis (EDA)")

# Display summary statistics
print(df.describe())

# 3. Data Aggregation and Grouping
print("\n3. Data Aggregation and Grouping")

# Calculate total sales
total_sales = df['SALES'].sum()
print(f"Total Sales: ${total_sales:,.2f}")

# Calculate average sales per customer
avg_sales_per_customer = df.groupby('CUSTOMERNAME')['SALES'].mean()
print("\nTop 5 customers by average sales:")
print(avg_sales_per_customer.sort_values(ascending=False).head())

# Calculate sales by product line
sales_by_productline = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
print("\nSales by Product Line:")
print(sales_by_productline)

# 4. Visualization
print("\n4. Visualization")

# Instead of using style.use(), we'll use basic matplotlib settings
plt.rcParams['figure.figsize'] = [12, 6]
plt.rcParams['axes.grid'] = True

# Plot 1: Sales by Product Line (Bar Chart)
plt.figure()
sales_by_productline.plot(kind='bar')
plt.title('Sales by Product Line', pad=20)
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Monthly Sales Trend (Line Chart)
plt.figure()
monthly_sales = df.groupby(df['ORDERDATE'].dt.to_period('M'))['SALES'].sum()
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend', pad=20)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Distribution of Order Quantities (Histogram)
plt.figure()
plt.hist(df['QUANTITYORDERED'], bins=30, edgecolor='black')
plt.title('Distribution of Order Quantities', pad=20)
plt.xlabel('Quantity Ordered')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# 5. Key Insights
print("\n5. Key Insights")
print("1. The product line with the highest sales is:", sales_by_productline.index[0])
print("2. The average order value is: ${:.2f}".format(df['SALES'].mean()))
print("3. The month with the highest sales is:", monthly_sales.idxmax())
print("4. The most common deal size is:", df['DEALSIZE'].mode()[0])
print("5. The top-selling product code is:", df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().idxmax())