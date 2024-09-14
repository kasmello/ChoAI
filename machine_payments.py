import pandas as pd

# Read the Excel file
def main():
    df = pd.read_excel('RawData/machine_order_list.xlsx')

    # Keep only columns 1, 4, 7, 8, 10 (Pandas is 0-indexed, so adjust accordingly)
    df_filtered = df.iloc[:, [0, 3, 6, 7, 8, 9]]

    # Rename the columns to 'ID', 'Machine', 'total', 'price', 'datetime'
    df_filtered.columns = ['ID', 'Machine', 'base', 'quantity', 'total','datetime']
    df_filtered['product']=df_filtered['Machine'].apply(lambda x: x + ' Machine')
    df_filtered['type']='Photo'

    df_filtered['datetime'] = pd.to_datetime(df_filtered['datetime'], format='%Y-%m-%d %H:%M:%S')
    # Display the result
    df_filtered.to_csv('ProcessedData/machine_order_list.csv',index=False)