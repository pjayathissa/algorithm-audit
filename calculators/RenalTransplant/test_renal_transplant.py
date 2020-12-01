import pytest
import pandas as pd
import os
import calculator_renal_transplant as cal

# import validation_renal_transplant as val
# import fetch_data_renal_transplant as fd

path = os.getcwd()
date_cols = ['date_accepted', 'date_first_rrt', 'date_referred_to_txCtr']
testfile = pd.read_csv(path + r'\calculators\RenalTransplant\test_suite_data_renal_transplant.csv',
                       parse_dates=date_cols)


class TestCalculator:
    def test_score_albumin(self):
        albumin_test_data = list(testfile.albumin_data)
        albumin_test_values = list(testfile.albumin_test)
        for i in range(len(albumin_test_data)):
            assert cal.score_albumin(albumin_test_data[i]) == albumin_test_values[i], "albumin is calculated wrong"

    def test_calc_bmi(self):
        height_test_data = list(testfile.height_data)
        weight_test_data = list(testfile.weight_data)
        bmi_test_value = list(testfile.bmis)
        for i in range(len(bmi_test_value)):
            assert cal.calc_bmi(height_test_data[i], weight_test_data[i]) == bmi_test_value[i],\
                "The BMI is calculated wrong for " + str(height_test_data[i]) + ' ' + str(weight_test_data[i])

    def test_score_bmi(self):
        bmi_test_data = list(testfile.bmi_data)
        bmi_test_values = list(testfile.bmi_test)
        for i in range(len(bmi_test_data)):
            assert cal.score_bmi(bmi_test_data[i]) == bmi_test_values[i], "BMI score doesn't match"

    def test_score_cause(self):
        cause_test_data = list(testfile.cause_data)
        cause_test_values = list(testfile.cause_test)
        for i in range(len(cause_test_data)):
            assert cal.score_cause(cause_test_data[i]) == cause_test_values[i], "Score of cause doesn't match"

    def test_score_history(self):
        history_diagnosis_data = list(testfile.history_diagnosis_data)
        history_result_data = list(testfile.history_result_data)
        history_test_data = list(testfile.history_test)
        for i in range(len(testfile.history_diagnosis_data)):
            assert cal.score_history(history_result_data[i], history_diagnosis_data[i]) == history_test_data[i], \
                "Score history doesn't match"

    def test_score_age(self):
        age_test_data = list(testfile.age_data)
        age_test_value = list(testfile.age_test)
        for i in range(len(age_test_data)):
            assert cal.score_age(age_test_data[i]) == age_test_value[i], "Age value doesn't match"

    def test_score_ethnicity(self):
        ethinicity_test_data = list(testfile.ethnicity_data)
        ethinicity_test_value = list(testfile.ethnicity_test)
        for i in range(len(ethinicity_test_data)):
            assert cal.score_ethnicity(ethinicity_test_data[i]) == ethinicity_test_value[i], "Wrong Ethnicity score" + \
                                                                                             ethinicity_test_data[i]

    def test_score_first_rrt(self):
        first_rrt_test_data = list(testfile.first_rrt_data)
        first_rrt_test_value = list(testfile.first_rrt_test)
        for i in range(len(first_rrt_test_data)):
            assert cal.score_first_rrt(first_rrt_test_data[i]) == first_rrt_test_value[i], "The first rrt score " \
                                                                                           "doesn't match"

    def test_score_timefrom_frtt(self):
        time_from_frtt_test_data = list(testfile.timefrom_frtt_data)
        time_from_frtt_test_value = list(testfile.timefrom_frtt_test)
        for i in range(len(time_from_frtt_test_data)):
            assert cal.score_time_from_frtt(time_from_frtt_test_data[i]) == time_from_frtt_test_value[i]

    def test_calculate(self):

        assert (testfile.apply(lambda x: cal.calculate(x['height_data'], x['weight_data'], x['date_accepted'],
                                                       x['date_first_rrt'], x['date_referred_to_txCtr'],
                                                       x['albumin_data'], x['cause_data'], x['age_data'],
                                                       x['ethnicity_data'], x['COPD'], x['Nonambulatory'], x['CHF'],
                                                       x['Insulin'], x['CAD'], x['PVD'], x['CVD'], x['HT'],
                                                       x['SmokerCurrent'], x['Employed']),
                               axis=1) == testfile.Survival_Factor).all(), "The renal transplant score doesn't match"

# class TestFetchData:
#     def test_fetch_data():
#     def test_create_connection():
#     def test_query_data():
#     def test_clean_data():
#
# class TestMain:
#     def test_renal_transplant(self):
#
# class TestValidation:
#     def test_validation(self):
#     def test_update_report(self):
#     def test_validate_bmi(self):
#     def test_validate_score(self):
