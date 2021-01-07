import calculator_dvt as cal
import pandas as pd
import numpy as np
import math
from datetime import datetime


# main validation function
def validation(numeric_results_df):
    dvt_audit_value = numeric_results_df.apply(lambda x: cal.calculate(x['DVTMalig'], x['DVTImmob'], x['DVTBed'],
                                                                       x['DVTTender'], x['DVTSwollen'], x['DVTCircum'],
                                                                       x['DVTOedema'], x['DVTCollateral'], x['DVTHist'],
                                                                       x['DVTAltDiag']), axis=1)
    validation_report = check_column(numeric_results_df['NMPI'], 'DVT WELLS SCORE', numeric_results_df['DVTWELLS'],
                                     dvt_audit_value, 'DVT WELLS', numeric_results_df['TESTDATE'])

    return validation_report.dropna(subset=['Result'])


# function to create the validation data frame
def check_column(id_num, column_name, submitted_value, audit_value, calculator_name, date_completed):
    result_df = pd.DataFrame()
    result_df['NMPI'] = id_num
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
