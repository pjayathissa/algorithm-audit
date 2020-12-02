import calculator_renal_transplant as cal
import pandas as pd
import numpy as np


# function to create the audit report
def validation(numeric_results_df):
    # validate bmi calculation
    result_df_bmi = pd.DataFrame()
    result_df_bmi['Live Value'] = numeric_results_df['bmis']
    result_df_bmi['Column Name'] = 'BMI'
    result_df_bmi['Audit Value'] = numeric_results_df.apply(lambda x: cal.calc_bmi(x['Height'], x['Weight']), axis=1)
    result_df_bmi['Result'] = result_df_bmi.apply(lambda x: validate(x['Column Name'], x['Live Value'],
                                                                     x['Audit Value']), axis=1)

    # validate renal score
    result_df_renal = pd.DataFrame()
    result_df_renal['Live Value'] = numeric_results_df['Survival_Factor']
    result_df_renal['Column Name'] = 'Renal Transplant Survival Score'
    result_df_renal['Audit Value'] = numeric_results_df.apply(
        lambda x: cal.calculate(height=x['Height'], weight=x['Weight'], date_accepted=x['dateAccepted'],
                                date_first_rrt=x['dateFirstRRT'], date_referred_to_txCtr=x['dateReferredtoTxCtr'],
                                albumin=x['Albumin'], cause=x['Cause'], age=x['Age'],
                                ethinic_group=x['EthnicGroup'], copd=x['COPD'], nonambulatory=x['Nonambulatory'],
                                chf=x['CHF'], insulin=x['Insulin'], cad=x['CAD'], pvd=x['PVD'], cvd=x['CVD'],
                                ht=x['HT'], smoker_current=x['SmokerCurrent'], employed=x['Employed']), axis=1)

    result_df_renal['Result'] = result_df_renal.apply(lambda x: validate(x['Column Name'], x['Live Value'],
                                                                         x['Audit Value']), axis=1)

    validation_report = pd.concat([result_df_renal, result_df_bmi])
    validation_report['Calculator Name'] = 'Renal Transplant Calculator'
    return validation_report.dropna(subset=['Result'])


# function to validate the values
def validate(target_column, acutal_value, audit_value):
    if acutal_value != audit_value:
        return "The " + target_column + " live value doesn't match audit value"
    else:
        return np.nan
