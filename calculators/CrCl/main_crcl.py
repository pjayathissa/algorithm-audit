import fetch_data_crcl as fd
import validation_crcl as val


def renal_transplant():
    datafile = fd.fetch_data()
    return val.validation(datafile)

# add exception handeling for null values
