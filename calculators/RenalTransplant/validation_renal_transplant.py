import calculator_renal_transplant as cal
import pandas as pd
import numpy as np


# main validation function
def validation(numeric_results_df):
    validation_report = []
    # validate bmi calculation
    bmi_audit_value = numeric_results_df.apply(lambda x: cal.calc_bmi(x['Height'], x['Weight']), axis=1)
    validation_report.append(check_column('BMI', numeric_results_df['bmis'], bmi_audit_value, 'Renal Transplant'))

    # validate renal score
    survival_score_audit_value = numeric_results_df.apply(
        lambda x: cal.calculate(height=x['Height'], weight=x['Weight'], date_accepted=x['dateAccepted'],
                                date_first_rrt=x['dateFirstRRT'], date_referred_to_txCtr=x['dateReferredtoTxCtr'],
                                albumin=x['Albumin'], cause=x['Cause'], age=x['Age'],
                                ethinic_group=x['EthnicGroup'], copd=x['COPD'], nonambulatory=x['Nonambulatory'],
                                chf=x['CHF'], insulin=x['Insulin'], cad=x['CAD'], pvd=x['PVD'], cvd=x['CVD'],
                                ht=x['HT'], smoker_current=x['SmokerCurrent'], employed=x['Employed']), axis=1)
    validation_report.append(check_column('Survival Factor', numeric_results_df['Survival_Factor'],
                                          survival_score_audit_value, 'Renal Transplant'))

    # joining the results into a single data frame
    validation_report = pd.concat(validation_report)
    return validation_report.dropna(subset=['Result'])


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
