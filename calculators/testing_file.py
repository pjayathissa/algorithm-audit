#calculator

#
# import pandas as pd
# import os
# path = os.getcwd()
# date_cols = ['date_accepted', 'date_first_rrt', 'date_referred_to_txCtr']
# testfile = pd.read_csv(path + r'\test_suite_data_renal_transplant.csv', parse_dates=date_cols)
# print(testfile.apply(lambda x: calc_bmi(x['height_data'], x['weight_data']), axis=1))
# print(testfile.apply(lambda x: calculate(x['height_data'], x['weight_data'], x['date_accepted'],
#                                          x['date_first_rrt'], x['date_referred_to_txCtr'],
#                                          x['albumin_data'], x['cause_data'], x['age_data'],
#                                          x['ethnicity_data'], x['COPD'], x['Nonambulatory'], x['CHF'],
#                                          x['Insulin'], x['CAD'], x['PVD'], x['CVD'], x['HT'],
#                                          x['SmokerCurrent'], x['Employed']), axis=1))


# validation

# import os
# path = os.getcwd()
# date_cols= ['date_accepted', 'date_first_rrt', 'date_referred_to_txCtr']
# testfile = pd.read_csv(path + r'\test_suite_data_renal_transplant.csv', parse_dates=date_cols)
# x = pd.DataFrame()
#
# x['Height'] = testfile['height_data']
# x['Weight']=testfile['weight_data']
# x['dateAccepted'] = testfile['date_accepted']
# x['dateFirstRRT']= testfile['date_first_rrt']
# x['dateReferredtoTxCtr']= testfile['date_referred_to_txCtr']
# x['Albumin']=testfile['albumin_data']
# x['Cause'] =testfile['cause_data']
# x['Age'] = testfile['age_data']
# x['EthnicGroup']=testfile['ethnicity_data']
# x['COPD']=testfile['COPD']
# x['Nonambulatory']=testfile['Nonambulatory']
# x['CHF']=testfile['CHF']
# x['Insulin']=testfile['Insulin']
# x['CAD']=testfile['CAD']
# x['PVD']=testfile['PVD']
# x['CVD']=testfile['CVD']
# x['HT']=testfile['HT']
# x['Survival_Factor'] = testfile['Survival_Factor']
# x['SmokerCurrent']=testfile['SmokerCurrent']
# x['Employed']=testfile['Employed']
# x['bmis']=testfile['bmis']
#
# print(validation(x))
