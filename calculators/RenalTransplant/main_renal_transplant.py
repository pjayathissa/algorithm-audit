import fetch_data_renal_transplant as fd
import validation_renal_transplant as val


def renal_transplant():
    datafile = fd.fetch_data()
    return val.validation(datafile)

# add exception handeling for null values
