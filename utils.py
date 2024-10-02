import pandas as pd
from config import DB_DETAILS
import sqlite3
import psycopg2

def load_db_details(env):
    return DB_DETAILS[env]

def get_sqlite3_connection(db_name) -> sqlite3.connect:
    try:
        connection = sqlite3.connect(db_name)
        return connection

    except Exception as error:
        print(error)
    
def get_postgres_connection(db_cred):
    try:
        connection = psycopg2.connect(db_cred)
        return connection
    
    except Exception as error:
        print(error)



def get_tables(path):
    tables = pd.read_csv(path,sep=':')
    return tables.query("to_be_loaded == 'yes'")