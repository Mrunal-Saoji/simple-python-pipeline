from utils import get_postgres_connection


def build_insert_query(table_name,column_name,data):
    column_name_str = ",".join(column_name)
    query = f"""
        INSERT INTO {table_name} ({column_name_str})
        VALUES (%s,%s,%s)
    """

    return query

def write_to_table(table_name,data,column_name,db_details):
    TARGET_DB = db_details['TARGET_DB']['POSTGRES_URL']

    connection = get_postgres_connection(TARGET_DB)
    cur = connection.cursor()
    query = build_insert_query(table_name=table_name,column_name=column_name,data=data)
    cur.executemany(query,data)
    print("success")
    connection.commit()
    connection.close()