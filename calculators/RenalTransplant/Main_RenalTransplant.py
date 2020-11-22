import FetchData_RenalTransplant as fd
import Validation_RenalTransplant as val

def renal_transplant():
    datafile=fd.fetch_data()
    return val.validation(datafile)
    #add exception handeling for null values





