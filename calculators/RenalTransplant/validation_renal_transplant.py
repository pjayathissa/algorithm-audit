import calculator_renal_transplant as cal


# function to create the audit report
def validation(numeric_results_df):
    return validate_score(validate_bmi(numeric_results_df))


# function to add comments to the dataset
def update_report(existing_comment, additional_comment):
    if existing_comment != ' ':
        return existing_comment+' and '+additional_comment
    else:
        return additional_comment


# function to validate the bmi calculations
def validate_bmi(numeric_results_df):
    bmi_series = cal.calc_bmi(height=numeric_results_df['Height'], weight=numeric_results_df['Weight'])
    # finding the incorrect bmi calculations
    validation_report = numeric_results_df.copy()
    validation_report['comments'] = ' '

    validation_report.loc[bmi_series - validation_report['bmis'] > 0, 'comments'] =\
        validation_report[bmi_series - validation_report['bmis'] > 0].comments.apply(
            lambda x: update_report(x, 'incorrect bmi calculation'))

    # bmi_series[bmi_series - numeric_results_df['bmis'] > 0]
    # finding out of bound bmi calculations
    validation_report.loc[validation_report['bmis'] > 200, 'comments'] = validation_report[
        validation_report['bmis'] > 200].comments.apply(lambda x: update_report(x, 'bmi out of bounds'))
    # finding incorrect height entered
    validation_report.loc[validation_report['Height'] < 10, 'comments'] = validation_report[
        validation_report['Height'] < 10].comments.apply(
        lambda x: update_report(x, 'possible wrong height entered'))

    validation_report['test_bmi'] = bmi_series

    return validation_report


# function to validate the score
def validate_score(numeric_results_df):
    scored_df = cal.calculate(numeric_results_df)
    # validation_report=numeric_results_df.copy()
    # add comments to paitents with incorrect calculations
    numeric_results_df['test_Survival_Factor'] = scored_df['test_Survival_Factor']
    numeric_results_df['diff_Survival_Factor'] = scored_df['diff_Survival_Factor']
    numeric_results_df.loc[numeric_results_df['test_Survival_Factor'] - numeric_results_df['Survival_Factor'] != 0,
                           'comments'] = numeric_results_df[numeric_results_df['test_Survival_Factor'] -
                                                            numeric_results_df['Survival_Factor'] != 0].comments.apply(
        lambda x: update_report(x, 'These patients have incorrect calculations'))

    # numeric_results_df[scored_df['test_Survival_Factor'] - scored_df['calc_Survival_Factor'] != 0].to_csv(
    #     'test_failed.csv')

    # Check what patients had an uderestimate of survival
    numeric_results_df.loc[numeric_results_df['test_Survival_Factor'] - numeric_results_df['Survival_Factor'] < 0,
                           'comments'] = numeric_results_df[numeric_results_df['test_Survival_Factor'] -
                                                            numeric_results_df['Survival_Factor'] < 0]. \
        comments.apply(lambda x: update_report(x, 'These patients have underestimate of survival'))

    # check what columns have null values
    numeric_results_df.loc[scored_df.isnull().any(axis=1), 'comments'] =\
        numeric_results_df[scored_df.isnull().any(axis=1)].comments.apply(lambda x: update_report(x, 'missing value'))
    # numeric_results_df[scored_df.isnull().any(axis=1)].to_csv('missing_value.csv')
    numeric_results_df.loc[scored_df['Cause'].isnull(), 'comments'] =\
        numeric_results_df[scored_df['Cause'].isnull()].comments.apply(lambda x: update_report(x, 'missing cause'))
    # numeric_results_df[scored_df['Cause'].isnull()].to_csv('missing_cause.csv')
    numeric_results_df.loc[scored_df['Employed'].isnull(), 'comments'] =\
        numeric_results_df[scored_df['Employed'].isnull()].comments.apply(lambda x: update_report(x, 'missing employed')
                                                                          )
    # numeric_results_df[scored_df['Employed'].isnull()].to_csv('missing_employed.csv')
    numeric_results_df.loc[scored_df['HT'].isnull(), 'comments'] =\
        numeric_results_df[scored_df['HT'].isnull()].comments.apply(lambda x: update_report(x, 'missing ht'))
    # numeric_results_df[scored_df['HT'].isnull()].to_csv('missing_ht.csv')
    numeric_results_df.loc[scored_df['bmis'].isnull(), 'comments'] =\
        numeric_results_df[scored_df['bmis'].isnull()].comments.apply(lambda x: update_report(x, 'missing bmis'))
    # numeric_results_df[scored_df['bmis'].isnull()].to_csv('missing_bmi.csv')

    return numeric_results_df
