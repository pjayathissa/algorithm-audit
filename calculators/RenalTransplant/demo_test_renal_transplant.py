import pandas as pd
import numpy as np
import calculator_renal_transplant as cal
import validation_renal_transplant as val
import fetch_data_renal_transplant as fd

def clean_data(result_df):
    numeric_results_df = result_df.copy()

    numeric_cols = ['Age', 'Albumin', 'bmis', 'Height', 'Weight', 'Survival_Factor']
    numeric_results_df[numeric_cols] = numeric_results_df[numeric_cols].apply(pd.to_numeric, downcast='float',
                                                                              errors='ignore')
    numeric_results_df['dateAccepted'] = pd.to_datetime(numeric_results_df['DateAccepted'], dayfirst=True)
    numeric_results_df['dateFirstRRT'] = pd.to_datetime(numeric_results_df['DateFirstRRT'], dayfirst=True)
    numeric_results_df['dateReferredtoTxCtr'] = pd.to_datetime(numeric_results_df['DateReferredtoTxCtr'], dayfirst=True)
    numeric_results_df.drop(['DateAccepted', 'DateFirstRRT', 'DateReferredtoTxCtr'], axis=1, inplace=True)

    return numeric_results_df


fileLink=r'C:\Users\udit sharma\Desktop\algorithm-audit\calculators\RenalTransplant\test_data_renal_transplant.csv'
dataframe=clean_data(pd.read_csv(fileLink))
print(dataframe.head())




print( val.validation(dataframe))
#     #add exception handeling for null values
# print(cal.calc_bmi(height=dataframe['Height'], weight=dataframe['Weight']))
#
#












# import numpy as np
# data={'bmis':[1,20,30,40,100,1000,1000],
#       'Height':[1,160,13,150,149,132,1]}
# numeric_results_df=pd.DataFrame(data)
# print(numeric_results_df)
# def add_comment(existing_comment,additional_comment):
#     if(existing_comment!=' '):
#        return existing_comment+' and '+additional_comment
#     else:
#         return additional_comment
# validation_report=numeric_results_df.copy()
# validation_report['comments']=' '
# print(validation_report)
# validation_report['comments'] = validation_report['comments'].apply(
#     lambda x: add_comment(' ', 'incorrect bmi calculation'))
#
# # bmi_series[bmi_series - numeric_results_df['bmis'] > 0] ###### add the correct bmi calculations to the report
# # df1['feat'] = np.where(df1['stream'] == 2, 10,20)
# # validation_report['comments']=np.where(validation_report['bmis'] > 200,)
# print(validation_report)
# # finding out of bound bmi calculations
# validation_report.loc[validation_report['bmis'] > 200,'comments'] = validation_report[validation_report['bmis'] > 200].comments.apply(lambda x: add_comment(x,'bmi out of bounds'))
# print(validation_report)
# # finding incorrect height entered
# validation_report.loc[validation_report['Height'] < 10,'comments'] = validation_report[validation_report['Height'] < 10].comments.apply(
#     lambda x: add_comment(x, 'possible wrong height entered'))
#
# print(validation_report)

