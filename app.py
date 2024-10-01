import sys
from config import DB_DETAILS
from utils import get_tables


def main():
    """Program takes at least one argument"""
    env = sys.argv[1]
    db = DB_DETAILS[env]
    tables = get_tables('table_list.txt')

if __name__ == '__main__':
    main()