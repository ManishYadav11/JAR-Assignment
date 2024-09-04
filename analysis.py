import pandas as pd
# Load the dataset
file_path = 'WalmartSales.xlsx'  
df = pd.read_excel(file_path)
print("Dataset loaded successfully.")

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print("'Date' column converted to datetime format.")

# Calculate total sales (Revenue) per transaction
df['Total'] = df['Unit price'] * df['Quantity']
print("Total sales (Revenue) per transaction calculated and added as 'Total' column.")

# A. Performance of Sales and Revenue at the City and Branch Level
print("\nA. Performance of Sales and Revenue at the City and Branch Level:")
sales_revenue_city_branch = df.groupby(['City', 'Branch'])['Total'].sum().reset_index()
sales_revenue_city_branch.columns = ['City', 'Branch', 'Total Sales Revenue']
print(sales_revenue_city_branch.sort_values(by='Total Sales Revenue', ascending=False))

# B. Calculate the Average Price of an Item Sold at Each Branch
print("\nB. Average Price of an Item Sold at Each Branch:")
average_price_per_branch = df.groupby(['City', 'Branch'], group_keys=False).apply(
    lambda x: (x['Total'].sum() / x['Quantity'].sum())
).reset_index(name='Average Price Per Item')
print(average_price_per_branch.sort_values(by='Average Price Per Item', ascending=False))

# Extracting the month and year from the 'Date' column
df['Month'] = df['Date'].dt.to_period('M')
print("\nExtracted 'Month' from the 'Date' column to analyze month-over-month performance.")

# Verify available months to check for April 2019
print("\nAvailable Months in Dataset:", df['Month'].unique())

# C. Analyze Month-over-Month Performance Across Product Line, Gender, and Payment Method
print("\nC. Analyzing Month-over-Month Performance Across Product Line, Gender, and Payment Method:")
monthly_sales_analysis = df.groupby(['Month', 'Product line', 'Gender', 'Payment']).agg(
    total_sales=('Total', 'sum'),
    total_quantity=('Quantity', 'sum')
).reset_index()

# Display a sample of the monthly sales analysis data
print("\nSample Data from Monthly Sales Analysis:")
print(monthly_sales_analysis.head())

# Focus on the month of April 2019
april_2019_focus = monthly_sales_analysis[monthly_sales_analysis['Month'] == '2019-04']

# Check if the filtering is correct and print the results
if not april_2019_focus.empty:
    print("\nC. Performance for April 2019 across Product Line, Gender, and Payment Method:")
   
