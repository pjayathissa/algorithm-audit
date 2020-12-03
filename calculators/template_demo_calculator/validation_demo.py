# import calculator_demo as cal
import pandas as pd
import numpy as np


# main validation function
def validation(numeric_results_df):
    validation_report = []
    # call calculate function
    # call check column function
    return validation_report


# function to create the validation data frame
def check_column(column_name, live_value, audit_value, calculator_name):
    result_df = pd.DataFrame()
    result_df['Live Value'] = live_value
    result_df['Column Name'] = column_name
    result_df['Calculator Name'] = calculator_name
    result_df['Audit Value'] = audit_value
    result_df['Result'] = result_df.apply(lambda x: validate(x['Column Name'], x['Live Value'],
                                                             x['Audit Value']), axis=1)
    return result_df


# function to validate the values
def validate(target_column, actual_value, audit_value):
    if actual_value != audit_value:
        return "The " + target_column + " live value doesn't match audit value"
    else:
        return np.nan
