import pyodbc
import pandas as pd


# main function to fetch the data and clean it
def fetch_data():
    conn = create_connection()
    result_df = query_data('sql_scripts_crcl.sql', conn)
    return clean_data(result_df)


# function to create the connection with database
def create_connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=db_dw;'
                          'Database=DATADUMPS;'
                          'Trusted_Connection=yes;')

    return conn
# create a close connection function


# function to query the data
def query_data(filename, conn):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    return pd.read_sql_query(sqlFile, conn)


# function to clean the data
def clean_data(result_df):
    return 0
