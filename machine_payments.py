import pandas as pd

# Read the Excel file
df = pd.read_excel('data/machine_order_list.xlsx')

# Keep only columns 1, 4, 7, 8, 10 (Pandas is 0-indexed, so adjust accordingly)
df_filtered = df.iloc[:, [0, 3, 6, 7, 9]]

# Rename the columns to 'ID', 'Machine', 'total', 'price', 'datetime'
df_filtered.columns = ['ID', 'Machine', 'total', 'price', 'datetime']

df_filtered['datetime'] = pd.to_datetime(df_filtered['datetime'], format='%Y-%m-%d %H:%M:%S')
# Display the result
df_filtered.to_csv('data/machine_order_list.csv')