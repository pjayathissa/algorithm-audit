import fetch_data_possum as fd
import validation_possum as val


def p_possum():
    datafile = fd.fetch_data()
    return val.validation(datafile)


p_possum().to_csv('P_Possum_Audit_Report.csv')
