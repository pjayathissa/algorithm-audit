import calculator_renal_transplant as cal
import pandas as pd
import numpy as np
import math
from datetime import datetime


# main validation function
def validation(numeric_results_df):
    validation_report = []
    # validate bmi calculation
    bmi_audit_value = numeric_results_df.apply(lambda x: cal.calc_bmi(x['Height'], x['Weight']), axis=1)
    validation_report.append(check_column(numeric_results_df['NHI_number'], 'BMI', numeric_results_df['bmis'],
                                          bmi_audit_value.astype('float32'), 'Renal Transplant',
                                          numeric_results_df['date_completed']))

    # validate renal score
    survival_score_audit_value = numeric_results_df.apply(
        lambda x: cal.calculate(height=x['Height'], weight=x['Weight'], date_accepted=x['dateAccepted'],
                                date_first_rrt=x['dateFirstRRT'], date_referred_to_txCtr=x['dateReferredtoTxCtr'],
                                albumin=x['Albumin'], cause=x['Cause'], age=x['Age'],
                                ethinic_group=x['EthnicGroup'], copd=x['COPD'], nonambulatory=x['Nonambulatory'],
                                chf=x['CHF'], insulin=x['Insulin'], cad=x['CAD'], pvd=x['PVD'], cvd=x['CVD'],
                                ht=x['HT'], smoker_current=x['SmokerCurrent'], employed=x['Employed']), axis=1)
    validation_report.append(check_column(numeric_results_df['NHI_number'], 'Survival Factor',
                                          numeric_results_df['Survival_Factor'],
                                          survival_score_audit_value.astype('float32'), 'Renal Transplant',
                                          numeric_results_df['date_completed']))

    # joining the results into a single data frame
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
