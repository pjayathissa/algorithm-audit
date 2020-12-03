import fetch_data_dvt as fd
import validation_dvt as val


def renal_transplant():
    datafile = fd.fetch_data()
    return val.validation(datafile)

# add exception handeling for null values
