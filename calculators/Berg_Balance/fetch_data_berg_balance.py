import pyodbc
import pandas as pd


# main function to fetch the data and clean it
def fetch_data():
    conn = create_connection()
    result_df = query_data('sql_scripts_berg_balance.sql', conn)

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
    sql_file = fd.read()
    fd.close()

    return pd.read_sql_query(sql_file, conn)


# function to clean the data
def clean_data(result_df):
    numeric_results_df = result_df.copy()
    numeric_cols = ['BergItem9', 'BergItem12', 'BergItem8', 'BergItem1', 'BergItem3', 'BergItem14', 'BergItem4',
                    'BergItem2', 'BergItem13', 'BergItem6', 'BergItem7', 'Total_Score', 'BergItem5', 'BergItem11',
                    'BergItem10']
    numeric_results_df[numeric_cols] = numeric_results_df[numeric_cols].apply(pd.to_numeric, downcast='float',
                                                                              errors='ignore')
    return numeric_results_df
