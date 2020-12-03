import calculator_IgA as cal
import pandas as pd
import numpy as np


# main validation report
def validation(numeric_results_df):
    validation_report = []
    # validate Mean arterial pressure
    map_audit_value = numeric_results_df.apply(lambda x: cal.calculate_map(x['systoic_bp'],
                                                                           x['diastoic_bp']))
    validation_report.append(check_column('MAP', numeric_results_df['MAP'], map_audit_value, 'IgA'))

    # calculate the predicted risk
    predicted_risk_1_audit_value, predicted_risk_3_audit_value, predicted_risk_5_audit_value = \
        numeric_results_df.apply(lambda x: cal.calculate(x))

    # validate predicted risk year 1
    validation_report.append(check_column('Predicted Risk Year 1', numeric_results_df['Year 1'],
                                          predicted_risk_1_audit_value, 'IgA'))
    # validate predicted risk year 3
    validation_report.append(check_column('Predicted Risk Year 3', numeric_results_df['Year 3'],
                                          predicted_risk_1_audit_value, 'IgA'))
    # validate predicted risk year 5
    validation_report.append(check_column('Predicted Risk Year 1', numeric_results_df['Year 5'],
                                          predicted_risk_1_audit_value, 'IgA'))

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
