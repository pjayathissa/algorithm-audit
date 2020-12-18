import math


# function to calculate berg balance outcome
def calculate(berg_score):
    berg_outcome_list = {"No aids": 0, "Walking stick outdoors": 1, "Walking stick indoors": 2, "Walking frame": 3,
                         "Null": 4}
    if berg_score == 49:
        berg_outcome = berg_outcome_list["No aids"]
    elif berg_score == 48:
        berg_outcome = berg_outcome_list["Walking stick outdoors"]
    elif berg_score == 45:
        berg_outcome = berg_outcome_list["Walking stick indoors"]
    elif berg_score == 33:
        berg_outcome = berg_outcome_list["Walking frame"]
    else:
        berg_outcome = berg_outcome_list["Null"]

    return berg_outcome


# function to find berg score
def calc_berg_score(berg_items_list):
    berg_score = 0
    for berg_items in berg_items_list:
        if not math.isnan(berg_items):
            berg_score += berg_items

    return berg_score


# function to convert berg outcome to numeric values
def convert_berg_outcome_numeric(berg_outcome):
    berg_outcome_list = {"No aids": 0, "Walking stick outdoors": 1, "Walking stick indoors": 2, "Walking frame": 3,
                         None: 4}

    return berg_outcome_list[berg_outcome]
