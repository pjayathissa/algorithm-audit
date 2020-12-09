# main function to calculate whether treatment is required or not
def calculate(active_cancer, paralysis, recent_bedridden, localized_tenderness, swelling_of_leg, calf_swelling,
              pitting_edema, collateral_superficial_veins, previous_dvt, alternate_diagnosis):
    score = score_dvt_func(active_cancer, paralysis, recent_bedridden, localized_tenderness, swelling_of_leg,
                           calf_swelling, pitting_edema, collateral_superficial_veins, previous_dvt, alternate_diagnosis
                           )
    return score
    # if score >= 2:
    #     return 1
    # elif score < 2:
    #     return 0
    # else:
    #     return np.nan  # return error or null


# function to score dvt
def score_dvt_func(active_cancer, paralysis, recent_bedridden, localized_tenderness, swelling_of_leg, calf_swelling,
                   pitting_edema, collateral_superficial_veins, previous_dvt, alternate_diagnosis):
    score = 0
    if active_cancer:
        score += 1
    # if (Paralysis, paresis or recent plaster):
    if paralysis:
        score += 1
    # if (recent bedridden > 3 days or major surgert within 12 weeks requiring general or reginoal anaesthesia):
    if recent_bedridden:
        score += 1
    # if (Localized tendreness along the distribution of deep venous system):
    if localized_tenderness:
        score += 1
    # if (swelling of entire leg):
    if swelling_of_leg:
        score += 1
    # if(calf swelling > 3 cm larger than asymptomatic side..measured 10 cm below tibial tuberosity):
    if calf_swelling:
        score += 1
    # if (Pitting edema confined to syptomatic leg):  ### paper suggest edema and the front end ask for oedema
    if pitting_edema:
        score += 1
    # if (Collateral superficial veins nonvaricose):
    if collateral_superficial_veins:
        score += 1
    if previous_dvt:
        score += 1
# if (Alternative diagnosis at least as likely as DVT):
    if alternate_diagnosis:
        score -= 2

    return score
