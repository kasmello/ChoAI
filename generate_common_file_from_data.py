import pandas as pd
import sqlite3
import json
from tqdm import tqdm
import square_extract, roster, machine_payments
import random

def scramble_columns_and_rows(df, state=120):
    # Scramble the columns by shuffling the column names, with a seed for reproducibility
    scrambled_columns = df.sample(frac=1, axis=1, random_state=state)
    
    # Scramble the rows by shuffling the index, with a seed for reproducibility
    scrambled_df = scrambled_columns.sample(frac=1, random_state=state).reset_index(drop=True)
    
    return scrambled_df

def scramble_names(df, column_name_staff, column_name_replaced, state=120):
    #choose random name from list and assign:
    name_list = [
    'Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'Sophia', 'William', 'Isabella',
    'James', 'Mia', 'Benjamin', 'Evelyn', 'Lucas', 'Harper', 'Henry', 'Camila', 'Alexander', 'Gianna',
    'Mason', 'Luna', 'Michael', 'Ella', 'Ethan', 'Elizabeth', 'Daniel', 'Sofia', 'Jacob', 'Avery',
    'Logan', 'Mila', 'Jackson', 'Aria', 'Levi', 'Scarlett', 'Sebastian', 'Penelope', 'Mateo', 'Layla',
    'Jack', 'Chloe', 'Owen', 'Victoria', 'Theodore', 'Madison', 'Aiden', 'Eleanor', 'Samuel', 'Grace',
    'Joseph', 'Nora', 'John', 'Riley', 'David', 'Zoey', 'Wyatt', 'Hannah', 'Matthew', 'Hazel',
    'Luke', 'Lily', 'Asher', 'Ellie', 'Carter', 'Violet', 'Julian', 'Lillian', 'Grayson', 'Zoe',
    'Leo', 'Stella', 'Jayden', 'Aurora', 'Gabriel', 'Natalie', 'Isaac', 'Emilia', 'Lincoln', 'Everly',
    'Anthony', 'Leah', 'Hudson', 'Aubrey', 'Dylan', 'Willow', 'Ezra', 'Addison', 'Thomas', 'Lucy',
    'Charles', 'Audrey', 'Christopher', 'Bella', 'Jaxon', 'Nova', 'Maverick', 'Brooklyn', 'Josiah', 'Paisley'
    ]
    random.seed(state)
    # Randomly pick a name for each unique name in the 'staff' column, ensuring no name repeats
    random_names = random.sample(name_list, len(df[column_name_staff].unique()))
    
    # Create a mapping from existing staff names to new random names
    name_mapping = dict(zip(df[column_name_staff].unique(), random_names))
    
    # Map the new random names to the 'staff' column
    df[column_name_staff] = df[column_name_staff].map(name_mapping)
    df[column_name_replaced] = df[column_name_replaced].map(name_mapping)
    
    return df, name_mapping

def column_changes(query, state=120):
    random.seed(state)
    staff = random.choice(['as staff','as employee','as worker'])
    replaced = random.choice(['as replaced','as original','as old','as original_staff','as old_staff'])
    action = random.choice(['as action','as action_time'])
    quantity = random.choice(['as quantity','as count'])

    query = query.replace('as staff',staff)
    query = query.replace('as replaced',replaced)
    query = query.replace('as action',action)
    query = query.replace('as quantity',quantity)
    return query, staff, replaced, action, quantity


def main():
    # square_extract.main()
    # roster.main(mask=False)
    # machine_payments.main()

    conn = sqlite3.connect(":memory:") 
    roster_df = pd.read_csv('ProcessedData/roster.csv')
    roster_df.to_sql("roster", conn, index=False)

    square = pd.read_csv('ProcessedData/square_payments.csv')
    square['datetime'] = pd.to_datetime(square['datetime'])
    square.to_sql("square", conn, index=False)

    machine = pd.read_csv('ProcessedData/machine_order_list.csv')
    machine['datetime'] = pd.to_datetime(machine['datetime'])
    machine.to_sql("machine", conn, index=False)

    #original

    

    qry = "SELECT \
        coalesce(roster.replacement,roster.staff) as staff\
        ,case when roster.replacement is not null then roster.staff end as replaced\
        ,substr(roster.date,7,4)||'-'||substr(roster.date,4,2)||'-'||substr(roster.date,1,2) as Date\
        ,square.datetime as action_time\
        ,square.name as product\
        ,square.type as type\
        ,square.quantity as quantity\
        ,square.base as base\
        ,square.total as total\
        FROM roster \
        LEFT JOIN square ON roster.start_datetime <= square.datetime and roster.end_datetime >= square.datetime\
        UNION\
        SELECT\
        coalesce(roster.replacement,roster.staff) as staff\
        ,case when roster.replacement is not null then roster.staff end as replaced\
        ,substr(roster.date,7,4)||'-'||substr(roster.date,4,2)||'-'||substr(roster.date,1,2) as Date\
        ,machine.datetime as action_time\
        ,machine.product as product\
        ,machine.type as type\
        ,machine.quantity as quantity\
        ,machine.base as base\
        ,machine.total as total\
        FROM roster \
        LEFT JOIN machine ON roster.start_datetime <= machine.datetime and roster.end_datetime >= machine.datetime\
        "
    
    
    qry_test = "select * from roster where strftime('%m', start_datetime)='06' order by start_datetime asc"
    random.seed(120)
    rand_seeds = [random.randint(1,1000) for _ in range(20)]
    df_column_desc = []
    for i in tqdm(range(20)):
        qry_modification, staff, replaced, action, quantity = column_changes(qry,state=rand_seeds[i])
        tt = pd.read_sql_query(qry_modification,conn)
        tt_modification = scramble_columns_and_rows(tt,state=rand_seeds[i])
        tt_modification, name_mapping = scramble_names(tt_modification,staff[3:], replaced[3:],state=rand_seeds[i])
        tt_modification.to_csv(f'ProcessedData/Joined_DF_{i}.csv',index=False)
        df_column_desc.append({
            'filename': f'ProcessedData/Joined_DF_{i}.csv', 
            'staff': staff[3:], 
            'replaced': replaced[3:], 
            'action': action[3:], 
            'quantity': quantity[3:],
            'Jess': name_mapping['Jess'],
            'Karmel': name_mapping['Karmel'],
            'Nicole': name_mapping['Nicole'],
            'Natalie': name_mapping['Natalie'],
            'Christiana': name_mapping['Christiana'],
            'Amanda': name_mapping['Amanda'],
            'Grace': name_mapping['Grace']})

    with open('ProcessedData/df_column_desc.txt','w+') as file:
        json.dump(df_column_desc, file, indent=4)


main()



