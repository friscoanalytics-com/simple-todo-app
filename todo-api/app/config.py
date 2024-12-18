import os
from urllib.parse import quote_plus

#  Database Configuration
sql_username = os.environ.get('SQL_USERNAME', 'root')
sql_password = os.environ.get('SQL_PASSWORD', '')
sql_server = os.environ.get('SQL_SERVER', 'localhost:3306')

sql_db_name = os.environ.get('SQL_DBNAME', '')

class AppConfig(object):
    # Configure your MySQL database connection
    encoded_password = quote_plus(sql_password)
    DATABASE_URL = f"mysql+pymysql://{sql_username}:{encoded_password}@{sql_server}/{sql_db_name}"
