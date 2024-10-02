from utils import get_sqlite3_connection
import pandas as pd


def read_table(db_details,table_name,limit=0):
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_sqlite3_connection(SOURCE_DB['DB_NAME'])
    cursor  = connection.cursor()

    if limit == 0 :
        query = f"SELECT * FROM {table_name}"
    else :
        query = f"SELECT * FROM {table_name} LIMIT {limit}"

    cursor.execute(query)
    data = cursor.fetchall()

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", connection)
    columns_name = df.columns.tolist()
    connection.close()

    return data,columns_name
