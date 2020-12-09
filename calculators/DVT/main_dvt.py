import fetch_data_dvt as fd
import validation_dvt as val
import pandas as pd


def dvt_wells():
    datafile = fd.fetch_data()
    return val.validation(datafile)


pd.DataFrame.to_csv(dvt_wells(), 'dvt_wells_score.csv')
