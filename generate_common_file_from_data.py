import pandas as pd
import sqlite3
import square_extract, roster, machine_payments

def main():
    square_extract.main()
    roster.main(mask=False)
    machine_payments.main()

    conn = sqlite3.connect(":memory:") 
    roster_df = pd.read_csv('ProcessedData/roster.csv')
    roster_df.to_sql("roster", conn, index=False)

    square = pd.read_csv('ProcessedData/square_payments.csv')
    square['datetime'] = pd.to_datetime(square['datetime'])
    square.to_sql("square", conn, index=False)

    machine = pd.read_csv('ProcessedData/machine_order_list.csv')
    machine['datetime'] = pd.to_datetime(machine['datetime'])
    machine.to_sql("machine", conn, index=False)


    qry = "SELECT \
        coalesce(roster.replacement,roster.staff) as staff\
        ,case when roster.replacement is not null then roster.staff end as replaced\
        ,roster.date\
        ,square.datetime as action_time\
        ,square.name as product\
        ,square.type as type\
        ,square.quantity as quantity\
        ,square.base as base\
        ,square.total as total\
        FROM roster \
        INNER JOIN square ON roster.start_datetime <= square.datetime and roster.end_datetime >= square.datetime\
        UNION\
        SELECT\
        coalesce(roster.replacement,roster.staff) as staff\
        ,case when roster.replacement is not null then roster.staff end as replaced\
        ,roster.date\
        ,machine.datetime as action_time\
        ,machine.product as product\
        ,machine.type as type\
        ,machine.quantity as quantity\
        ,machine.base as base\
        ,machine.total as total\
        FROM roster \
        INNER JOIN machine ON roster.start_datetime <= machine.datetime and roster.end_datetime >= machine.datetime\
        "
    qry_test = "select * from roster where strftime('%m', start_datetime)='06' order by start_datetime asc"
    tt = pd.read_sql_query(qry,conn)
    tt.to_csv('ProcessedData/Joined_DF.csv',index=False)
    print(tt)



