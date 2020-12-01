import numpy as np
import math


def score_albumin(albumin):
    if albumin < 25:  # end cases not accounted for yet like 0 or negative
        return 9
    elif 25 <= albumin < 28:
        return 7
    elif 28 <= albumin < 33:
        return 6
    elif 33 <= albumin < 38:
        return 5
    elif 38 <= albumin < 40:
        return 4
    elif 40 <= albumin <= 41:  # to be consistent with the calculator
        return 3
    elif 41 <= albumin:  # equal not needed.
        return 0
    else:
        return np.nan
    # raise Exception("issue with calc_albumin defnintion for value", albumin)


# function to calculate bmi
def calc_bmi(height, weight):
    bmi = weight / ((height / 100.0) ** 2)
    return round(bmi, 2)


# function to calculate score due to bmi
def score_bmi(bmi):
    if bmi <= 20.4:  # strict less than
        return 1
    elif 20.4 < bmi <= 25.0:  # should be equal here
        return 0
    elif 25.0 < bmi <= 35.7:
        return -1
    elif 35.7 < bmi:
        return 0
    else:
        return np.nan
        # raise Exception('issue with score_bmi for value', bmi)


# function to calculate score due to different causes
def score_cause(cause):
    causes_dict = {'Diabetes': 3,
                   'Hypertension': -1,
                   'GN': -4,
                   'APKD': -6,
                   'Other': 0}
    if cause in causes_dict:
        return causes_dict[cause]
    else:
        # print('causes', cause, 'not in dictionary')
        return np.nan


# function to calculate score due to history
def score_history(result, diagnosis):
    history_dict = {'COPD': 3,
                    'Nonambulatory': 3,
                    'CHF': 2,
                    'Insulin': 2,
                    'CAD': 2,
                    'PVD': 2,
                    'CVD': 1,
                    'HT': -1,
                    'SmokerCurrent': 3,
                    'Employed': -2}

    if result == 'Yes':
        return history_dict[diagnosis]
    elif result == 'No':
        return 0
    else:
        return np.nan
    # raise Exception('history field missing for',diagnosis,'value of',result)


# function to calculate score due to age
def score_age(age):
    if age < 31:
        return 0
    elif 31 <= age < 37.5:
        return 5
    elif 37.5 <= age < 42.5:
        return 8
    elif 42.5 <= age < 46.8:
        return 11
    elif 46.8 <= age < 50.3:
        return 13
    elif 50.3 <= age < 53.7:
        return 15
    elif 53.7 <= age < 57.0:
        return 17
    elif 57.0 <= age < 60.7:
        return 18
    elif 60.7 <= age < 65.3:
        return 21
    elif 65.3 <= age:
        return 28
    else:
        return np.nan
    # raise Exception('age field missing', age)


# function to define Ethnicity score
def score_ethnicity(ethnicity):
    if ethnicity in ['European', 'NZ European']:
        return 0
    elif ethnicity in ['Pacific Islander', 'Asian', 'Maori', 'Other']:
        return -4  # depends on data but not always -4
    else:
        return np.nan
    # raise Exception('Ethnicity Missing')


# score for first rrt year
def score_first_rrt(year):
    if year > 2001:
        return 1
    elif year <= 2001:
        return 0
    else:
        return np.nan
    # raise Exception('year of first RRT missing')


# score for time from first rtt
def score_time_from_frtt(months):
    if months <= 0.1:
        return 0
    elif 0.1 < months <= 0.5:  # what happens at 0.1
        return 6
    elif 0.5 < months <= 3.7:
        return 7
    elif 3.7 < months <= 6.0:
        return 8
    elif 6.0 < months <= 8.4:
        return 9
    elif 8.4 < months <= 11.3:
        return 10
    elif 11.3 < months <= 15.0:
        return 10
    elif 15.0 < months <= 20.7:
        return 11
    elif 20.7 < months <= 31.7:
        return 12
    elif 31.7 < months <= 75.1:
        return 15
    elif 75.1 < months:  # TODO question this
        return 15
    else:
        return np.nan
    # raise Exception('time from first rrt out of range', months)


# main calculate function
def calculate(height, weight, date_accepted, date_first_rrt, date_referred_to_txCtr, albumin, cause,
              age, ethinic_group, copd, nonambulatory, chf, insulin, cad, pvd, cvd,
              ht, smoker_current, employed):
    renal_score = 0
    bmi = calc_bmi(height, weight)
    history_list = ['COPD', 'Nonambulatory', 'CHF', 'Insulin', 'CAD', 'PVD', 'CVD', 'HT',
                    'SmokerCurrent', 'Employed']
    history = [copd, nonambulatory, chf, insulin, cad, pvd, cvd, ht, smoker_current, employed]
    months_to_accepted = (date_accepted - date_first_rrt) / np.timedelta64(1, 'M')
    months_to_referal = (date_referred_to_txCtr - date_first_rrt) / np.timedelta64(1, 'M')
    if(math.isnan(months_to_accepted)):
        months_to_listing = months_to_accepted
    else:
        months_to_listing = months_to_referal
    renal_score = score_albumin(albumin) + score_bmi(bmi) + score_cause(cause) + score_age(age) + score_ethnicity(
        ethinic_group) + score_first_rrt(date_first_rrt.year) + score_time_from_frtt(months_to_listing) - 26
    for i, history_diagnosis in enumerate(history):
        renal_score += score_history(history_diagnosis, history_list[i])

    return renal_score
