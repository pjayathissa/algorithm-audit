import calculator_berg_balance as cal
import pandas as pd
import numpy as np
import math
from datetime import datetime


# main validation function
def validation(numeric_results_df):
    validation_report = []

    # validate the berg score
    berg_score_audit_value = numeric_results_df.apply(lambda x: cal.calc_berg_score([x['BergItem9'],
                                                                                     x['BergItem12'],
                                                                                     x['BergItem8'],
                                                                                     x['BergItem1'],
                                                                                     x['BergItem3'],
                                                                                     x['BergItem14'],
                                                                                     x['BergItem4'],
                                                                                     x['BergItem2'],
                                                                                     x['BergItem13'],
                                                                                     x['BergItem6'],
                                                                                     x['BergItem7'],
                                                                                     x['BergItem5'],
                                                                                     x['BergItem11'],
                                                                                     x['BergItem10']]), axis=1)
    validation_report.append(check_column(numeric_results_df['NHI_number'], 'Berg Balance Score',
                                          numeric_results_df['Total_Score'],
                                          berg_score_audit_value.astype('float32'),
                                          'Berg Balance', numeric_results_df['date_completed']))

    # validate the berg outcome
    berg_outcome_audit_value = berg_score_audit_value.apply(cal.calculate)
    validation_report.append(check_column(numeric_results_df['NHI_number'], 'Berg Balance outcome',
                                          numeric_results_df['BergOutcome'].apply(cal.convert_berg_outcome_numeric),
                                          berg_outcome_audit_value.astype('float32'),
                                          'Berg Balance', numeric_results_df['date_completed']))

    validation_report = pd.concat(validation_report)
    return validation_report.dropna(subset=['Result'])


# function to create the validation data frame
def check_column(nhi_num, column_name, submitted_value, audit_value, calculator_name, date_completed):
    result_df = pd.DataFrame()
    result_df['NHI_number'] = nhi_num
    result_df['Calculator Name'] = calculator_name
    result_df['Column Name'] = column_name
    result_df['Date of Submission'] = date_completed
    result_df['Date of Audit'] = datetime.now()
    result_df['Submitted Value'] = submitted_value
    result_df['Audit Value'] = audit_value
    result_df['Result'] = result_df.apply(lambda x: validate(x['Column Name'], x['Submitted Value'],
                                                             x['Audit Value']), axis=1)

    return result_df


# function to validate the values
def validate(target_column, actual_value, audit_value):
    if math.isnan(actual_value) or math.isnan(audit_value):
        return "Required Arguments Missing"
    if actual_value != audit_value:
        return "The " + target_column + " live value doesn't match audit value"
    else:
        return np.nan
