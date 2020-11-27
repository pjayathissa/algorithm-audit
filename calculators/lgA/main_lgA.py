import fetch_data_demo as fd
import validation_demo as val


def renal_transplant():
    datafile = fd.fetch_data()
    return val.validation(datafile)

# add exception handeling for null values