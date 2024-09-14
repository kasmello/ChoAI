import pandas as pd

mask_names = {
    "Amanda": "Alex",
    "Christiana": "Bob",
    "Grace": "Catherine",
    "Jess": "Donald",
    "Karmel": "Eleven",
    "Natalie": "Forest",
    "Nicole": "Gary"
}

def main(mask):
    df = pd.read_csv('RawData/roster.csv')
    df['start_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Start'], dayfirst=True)
    df['end_datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Finish'], dayfirst=True)
    if mask:
        df["Staff"] = df["Staff"].apply(lambda x: mask_names[x])
    df.to_csv('ProcessedData/roster.csv',index=False)

if __name__ == '__main__':
    main(False)

