import pyodbc
import pandas as pd


# main function to fetch the data and clean it
def fetch_data():
    conn = create_connection()
    result_df = query_data('sql_scripts_dvt.sql', conn)

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
    column_list = ['DVTHist', 'DVTCircum', 'DVTMalig', 'DVTRisk', 'DVTTender', 'DVTAltDiag', 'DVTBed', 'DVTOedema',
                   'DVTWELLS', 'DVTSwollen', 'DVTCollateral', 'DVTImmob']

    dvt_data_list = []
    for nmpi_num in list(result_df.NMPI.unique()):
        for test_date in get_date(result_df, nmpi_num):
            temp_list = [nmpi_num, test_date]
            for col in column_list:
                temp_list.append(search_data(result_df, nmpi_num, col, test_date).values[0])
            dvt_data_list.append(temp_list)

    column_list = ['NMPI', 'TESTDATE', 'DVTHist', 'DVTCircum', 'DVTMalig', 'DVTRisk', 'DVTTender', 'DVTAltDiag',
                   'DVTBed', 'DVTOedema', 'DVTWELLS', 'DVTSwollen', 'DVTCollateral', 'DVTImmob']
    final_df = pd.DataFrame(data=dvt_data_list, columns=column_list)
    final_df = final_df.replace('likely', True)
    final_df = final_df.replace('unlikely', False)
    final_df = final_df.replace('Yes', True)
    final_df = final_df.replace('No', False)
    final_df['DVTWELLS'] = final_df['DVTWELLS'].apply(pd.to_numeric, downcast='float', errors='ignore')

    return final_df


# function to find the values of each column
def search_data(result_df, nmpi_num, col_name, test_date):
    temp_df = result_df[result_df['FIELDID'] == col_name]
    temp_df = temp_df[temp_df['TESTDATE'] == test_date]
    return temp_df[temp_df['NMPI'] == nmpi_num].RESULTTEXT


# function to find the test dates for patients
def get_date(result_df, nmpi_num):
    return result_df[result_df['NMPI'] == nmpi_num].TESTDATE
