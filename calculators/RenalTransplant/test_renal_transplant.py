import pytest
import calculator_renal_transplant as cal
import validation_renal_transplant as val
import fetch_data_renal_transplant as fd


class TestCalculator:
    def test_score_albumin(self):
        albumin_test_data=[24, 25, 27, 28, 31, 33, 35, 38, 39, 40, 41, 45]
        albumin_test_values=[9, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 0]
        for i,x in enumerate(albumin_test_data):
            assert cal.score_albumin(albumin_test_data[i]) == albumin_test_values[i], "albumin is calculated wrong"


    def test_calc_bmi(self):
        assert cal.calc_bmi(170, 70) == 24.22, "The BMI is calculated wrong"


    def test_score_bmi(self):
        assert cal.score_bmi(20.4) == 1, "BMI score doesn't match"


    def test_score_cause(self):
        assert cal.score_cause('Diabetes') == 3, "Score of cause doesn't match"

    def test_score_history(self):
        assert cal.score_history('Yes','Employed') == -2, "Score history doesn't match"

    def test_score_age(self):
        age_data = [29, 31, 35, 37.5, 40, 42.5, 45, 46.8, 47, 50.3, 51, 53.7, 55, 57, 58.6, 60.7, 62.3, 65.3,65.4]
        age_value = [0, 5, 5, 8, 8, 11, 11, 13, 13, 15, 15, 17, 17, 18, 18, 21, 21, 28, 28]
        for i in range(len(age_data)):
            assert cal.score_age(age_data[i]) == age_value[i], "Age value doesn't match for" + age_data[i]


    def test_score_ethnicity(self):
        ethinicity_data=['European', 'NZ European', 'Pacific Islander', 'Asian', 'Maori', 'Other']
        ethinicity_score=[0, 0, -4, -4, -4, -4]
        for i in range(len(ethinicity_data)):
            assert cal.score_ethnicity(ethinicity_data[i]) == ethinicity_score[i], "Wrong Ethnicity score" + \
                                                                                   ethinicity_data[i]
            #     def test_score_first_rrt():
#     def test_score_timefrom_frtt():
    def test_adjust_transplantation(self):
        assert cal.adjust_transplantation() == -26
    # def test_calculate(self):
    #     assert
#
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
#
