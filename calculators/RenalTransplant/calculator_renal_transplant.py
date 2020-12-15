import numpy as np
import math


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
    months_to_referral = (date_referred_to_txCtr - date_first_rrt) / np.timedelta64(1, 'M')
    if not math.isnan(months_to_accepted):
        months_to_listing = months_to_accepted
    else:
        months_to_listing = months_to_referral

    renal_score = score_albumin(albumin) + score_bmi(bmi) + score_cause(cause) + score_age(age) + score_ethnicity(
        ethinic_group) + score_first_rrt(date_first_rrt.year) + score_time_from_frtt(months_to_listing) - 26
    for i, history_diagnosis in enumerate(history):
        renal_score += score_history(history_diagnosis, history_list[i])

    return renal_score


# function to calculate 5 year survival score
def mortality_score_at_5yrs(renal_score):
    mortality_risk = {
        -47: 0.3,
        -46: 0.3,
        -45: 0.3,
        -44: 0.4,
        -43: 0.4,
        -42: 0.4,
        -41: 0.5,
        -40: 0.5,
        -39: 0.6,
        -38: 0.6,
        -37: 0.7,
        -36: 0.7,
        -35: 0.8,
        -34: 0.8,
        -33: 0.9,
        -32: 1,
        -31: 1.1,
        -30: 1.2,
        -29: 1.3,
        -28: 1.4,
        -27: 1.5,
        -26: 1.6,
        -25: 1.8,
        -24: 1.9,
        -23: 2.1,
        -22: 2.3,
        -21: 2.5,
        -20: 2.7,
        -19: 2.9,
        -18: 3.2,
        -17: 3.4,
        -16: 3.7,
        -15: 4,
        -14: 4.4,
        -13: 4.8,
        -12: 5.2,
        -11: 5.6,
        -10: 6.1,
        -9: 6.6,
        -8: 7.1,
        -7: 7.7,
        -6: 8.4,
        -5: 9.1,
        -4: 9.8,
        -3: 10.6,
        -2: 11.5,
        -1: 12.4,
        0: 13.4,
        1: 14.5,
        2: 15.7,
        3: 16.9,
        4: 18.2,
        5: 19.6,
        6: 21.2,
        7: 22.8,
        8: 24.5,
        9: 26.3,
        10: 28.2,
        11: 30.3,
        12: 32.4,
        13: 34.7,
        14: 37.1,
        15: 39.5,
        16: 42.1,
        17: 44.8,
        18: 47.6,
        19: 50.4,
        20: 53.4,
        21: 56.4,
        22: 59.4,
        23: 62.5,
        24: 65.5,
        25: 68.8,
        26: 71.6,
        27: 74.5,
        28: 77.4,
        29: 80.1,
        30: 82.7,
        31: 85.2,
        32: 87.4,
        33: 89.5,
        34: 91.4,
        35: 93,
        36: 94.5,
        37: 95.7,
        38: 96.7,
        39: 97.6,
        40: 98.2,
        41: 98.8,
        42: 99.2,
        43: 99.4
    }

    if -47 <= renal_score <= 43:
        return mortality_risk[renal_score]
    else:
        return np.nan


# function to score albumin
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
    # raise Exception("issue with calc_albumin definition for value", albumin)


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
