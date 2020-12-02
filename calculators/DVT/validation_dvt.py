# import calculator_dvt as cal
# import pandas as pd
import numpy as np


# function to create the audit report
def validation(numeric_results_df):
    # call validate function
    return 0


def validate(target_column, acutal_value, audit_value):
    if(acutal_value != audit_value):
        return "The " + target_column + " live value doesn't match audit value"
    else:
        return np.nan
