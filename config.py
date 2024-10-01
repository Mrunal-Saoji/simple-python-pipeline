import os
from dotenv import load_dotenv

load_dotenv()

DB_DETAILS = {
    'dev':{
        'SOURCE_DB': {
            'DB_TYPE': 'sqlite',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'retail_user',
            'DB_PASS': 'saoji'
        },
        'TARGET_DB': {
            'POSTGRES_URL' : os.environ.get('POSTGRES_URL')
        }
    }
}

