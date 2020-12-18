import fetch_data_berg_balance as fd
import validation_berg_balance as val


def berg_balance():
    datafile = fd.fetch_data()
    return val.validation(datafile)


# add exception handeling for null values
berg_balance().to_csv('Berg Balance Audit.csv')
