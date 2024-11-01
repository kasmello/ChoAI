import pandas as pd

def get_type(row):
    return 'Copy' if round(row['base'])==5 else 'Photo'
# Read the Excel file
def main(input='RawData/machine_order_list.xlsx',output='ProcessedData/machine_order_list.csv'):
    df = pd.read_excel(input)

    # Keep only columns 1, 4, 7, 8, 10 (Pandas is 0-indexed, so adjust accordingly)
    df_filtered = df.iloc[:, [0, 3, 6, 7, 8, 9]]

    # Rename the columns to 'ID', 'Machine', 'total', 'price', 'datetime'
    df_filtered.columns = ['ID', 'Machine', 'base', 'quantity', 'total','datetime']
    df_filtered['product']=df_filtered['Machine'].apply(lambda x: x + ' Machine')
    df_filtered['type']=df_filtered.apply(get_type, axis=1)

    df_filtered['datetime'] = pd.to_datetime(df_filtered['datetime'], format='%Y-%m-%d %H:%M:%S')
    # Display the result
    df_filtered.to_csv(output,index=False)

if __name__ == '__main__':
    main()