import pandas as pd


def main():
    df = pd.read_csv('RawData/roster2.csv')
    df['start_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Start'], dayfirst=True)
    df['end_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Finish'], dayfirst=True)
    df.to_csv('ProcessedData/roster.csv',index=False)

if __name__ == '__main__':
    main(False)

