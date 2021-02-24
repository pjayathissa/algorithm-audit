import calculator_possum as cal
import pandas as pd
import numpy as np
import math
from datetime import datetime




# main validation function
def validation(numeric_results_df):
    validation_report = []

    # validate the physiological score
    physiological_score_audit_value = numeric_results_df.apply(
        lambda x: cal.cal_physiological_score(x['Age'], x['Cardiac'], x['Respiratory'], x['SBP'], x['Pulse'], x['GCS'],
                                              x['Urea'], x['Sodium'], x['Potassium'], x['Haemoglobin'], x['WBC'],
                                              x['ECG'], x['NMPI']), axis=1)
    validation_report.append(check_column(numeric_results_df['NMPI'], 'Physiological Score',
                                          numeric_results_df['Physiology_Score'],
                                          physiological_score_audit_value.astype('float32'),
                                          'P-Possum', numeric_results_df['TESTDATE']))
    numeric_results_df['Physiology_Score_Audit_Value'] = physiological_score_audit_value

    # validate the operative severity score
    operative_score_audit_value = numeric_results_df.apply(
        lambda x: cal.cal_operative_score(x['Operation_Severity'], x['Number_of_Procedures'], x['Operative_Blood_Loss'],
                                          x['Peritoneal_Contamination'], x['Malignancy'], x['Urgency']), axis=1)
    validation_report.append(check_column(numeric_results_df['NMPI'], 'Operative Severity Score',
                                          numeric_results_df['Operative_Severity_Score'],
                                          operative_score_audit_value.astype('float32'),
                                          'P-Possum', numeric_results_df['TESTDATE']))
    numeric_results_df['Operative_Severity_Score_Audit_Value'] = operative_score_audit_value

    # validate mortality
    mortality_audit_value = numeric_results_df.apply(
        lambda x: cal.calculate_mortality(x['Physiology_Score_Audit_Value'], x['Operative_Severity_Score_Audit_Value']),
        axis=1)
    validation_report.append(check_column(numeric_results_df['NMPI'], 'Predicted Mortality',
                                          numeric_results_df['Predicted_Mortality'],
                                          mortality_audit_value.astype('float32'),
                                          'P-Possum', numeric_results_df['TESTDATE']))

    # validate morbidity
    morbidity_audit_value = numeric_results_df.apply(
        lambda x: cal.calculate_morbidity(x['Physiology_Score_Audit_Value'], x['Operative_Severity_Score_Audit_Value']),
        axis=1)
    validation_report.append(check_column(numeric_results_df['NMPI'], 'Predicted Morbidity',
                                          numeric_results_df['Predicted_Morbidity'],
                                          morbidity_audit_value.astype('float32'),
                                          'P-Possum', numeric_results_df['TESTDATE']))

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
