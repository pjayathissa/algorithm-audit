import calculator_IgA as cal
import pandas as pd
import numpy as np


# function to create the audit report
def validation(numeric_results_df):
    # validate Mean arterial pressure
    result_df_map = pd.DataFrame()
    result_df_map['Live Value'] = numeric_results_df['MAP']
    result_df_map['Column Name'] = 'MAP'
    result_df_map['Audit Value'] = numeric_results_df.apply(lambda x: cal.calculate_map(x['systoic_bp'],
                                                                                        x['diastoic_bp']))
    result_df_map['Result'] = result_df_map.apply(
        lambda x: validate(x['Column Name'], x['Live Value'], x['Audit Value']))

    # validate predicted risk year 1
    result_df_predicted_risk_1 = pd.DataFrame()
    result_df_predicted_risk_1['Live Value'] = numeric_results_df['Predicted Risk Year 1']
    result_df_predicted_risk_1['Column Name'] = 'Predicted Risk Year 1'
    # result_df_predicted_risk_1['Audit Value'] = numeric_results_df.apply(lambda x: cal.calculate_map(x))[0]
    result_df_predicted_risk_1['Result'] = result_df_predicted_risk_1.apply(
        lambda x: validate(x['Column Name'], x['Live Value'], x['Audit Value']))

    # validate predicted risk year 3
    result_df_predicted_risk_3 = pd.DataFrame()
    result_df_predicted_risk_3['Live Value'] = numeric_results_df['Predicted Risk Year 3']
    result_df_predicted_risk_3['Column Name'] = 'Predicted Risk Year 3'
    # result_df_predicted_risk_3['Audit Value'] = numeric_results_df.apply(lambda x: cal.calculate_map(x))[1]
    result_df_predicted_risk_3['Result'] = result_df_predicted_risk_3.apply(
        lambda x: validate(x['Column Name'], x['Live Value'], x['Audit Value']))

    # validate predicted risk year 5
    result_df_predicted_risk_5 = pd.DataFrame()
    result_df_predicted_risk_5['Live Value'] = numeric_results_df['Predicted Risk Year 5']
    result_df_predicted_risk_5['Column Name'] = 'Predicted Risk Year 5'
    # result_df_predicted_risk_5['Audit Value'] = numeric_results_df.apply(lambda x: cal.calculate_map(x))[2]
    result_df_predicted_risk_5['Result'] = result_df_predicted_risk_5.apply(
        lambda x: validate(x['Column Name'], x['Live Value'], x['Audit Value']))

    validation_report = pd.concat([result_df_map, result_df_predicted_risk_1, result_df_predicted_risk_3,
                                   result_df_predicted_risk_5])
    return validation_report.dropna(subset=['Result'])


def validate(target_column, acutal_value, audit_value):
    if (acutal_value != audit_value):
        return "The " + target_column + " live value doesn't match audit value"
    else:
        return np.nan
