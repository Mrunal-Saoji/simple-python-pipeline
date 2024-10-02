import sys
from config import DB_DETAILS
from utils import get_tables, load_db_details
from read import read_table
from write import write_to_table

def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db = load_db_details(env)
    tables = get_tables('table_list.txt')
    for  table in tables['table_name']:
        data , columns_name = read_table(db_details=db,table_name=table)
        print(data)
        print(columns_name)
        write_to_table(table_name=table,column_name=columns_name,data=data,db_details=db)


if __name__ == '__main__':
    main()