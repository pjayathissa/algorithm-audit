import fetch_data_IgA as fd
import validation_IgA as val


def renal_transplant():
    datafile = fd.fetch_data()
    return val.validation(datafile)

# add exception handeling for null values