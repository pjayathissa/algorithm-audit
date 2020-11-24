import pyodbc
import pandas as pd


# main function to fetch the data and clean it
def fetch_data():
    conn = create_connection()
    result_hdc = query_data('queryTransplantsHDC.sql', conn)
    result_npc = query_data('queryTransplantsNPC.sql', conn)
    result_pdc = query_data('queryTransplantsPDC.sql', conn)
    result_rtc = query_data('queryTransplantsRTC.sql', conn)
    # Combine dataframes to one
    result_df = pd.concat([result_hdc, result_npc, result_pdc, result_rtc])
    result_df = result_df[result_df['status'] == 'Completed']
    result_df.reset_index(inplace=True)

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
    numeric_results_df = result_df.copy()

    numeric_cols = ['Age', 'Albumin', 'bmis', 'Height', 'Weight', 'Survival_Factor']
    numeric_results_df[numeric_cols] = numeric_results_df[numeric_cols].apply(pd.to_numeric, downcast='float',
                                                                              errors='ignore')
    numeric_results_df['dateAccepted'] = pd.to_datetime(numeric_results_df['DateAccepted'], dayfirst=True)
    numeric_results_df['dateFirstRRT'] = pd.to_datetime(numeric_results_df['DateFirstRRT'], dayfirst=True)
    numeric_results_df['dateReferredtoTxCtr'] = pd.to_datetime(numeric_results_df['DateReferredtoTxCtr'], dayfirst=True)
    numeric_results_df.drop(['Survival_Probability_at_1yr', 'Survival_Probability_at_3yrs',
                             'Survival_Probability_at_5yrs', 'taskrequest_id', 'observation_report_id',
                             'stream_id', 'referralencounter', 'patient_programme_id',
                             'display_name'], axis=1, inplace=True)
    numeric_results_df.drop(['DateAccepted', 'DateFirstRRT', 'DateReferredtoTxCtr'], axis=1, inplace=True)

    return numeric_results_df
