import math


def calculate(egfr, systoic_bp, diastoic_bp, proteinuria, mesangial, endocapillary_hypercellilarity,
              segmental_sclerosis, tubular_atrophy, age, rasb, immunosuppression):
    map_val = calculate_map(systoic_bp, diastoic_bp)
    liner_pred = linear_predictor(egfr, map_val, proteinuria, mesangial, endocapillary_hypercellilarity,
                                  segmental_sclerosis, tubular_atrophy, age, rasb, immunosuppression)
    risk_year_1 = predict_risk(12, liner_pred)
    risk_year_3 = predict_risk(36, liner_pred)
    risk_year_5 = predict_risk(60, liner_pred)
    return risk_year_1, risk_year_3, risk_year_5


def linear_predictor(egfr, map, proteinuria, mesangial, endocapillary_hypercellilarity,
                     segmental_sclerosis, tubular_atrophy, age, rasb, immunosuppression):
    t1 = t2 = 0
    if(tubular_atrophy == 0):
        t1 = 0
        t2 = 0
    elif(tubular_atrophy == 1):
        t1 = 1
        t2 = 0
    elif(tubular_atrophy == 2):
        t1 = 0
        t2 = 1

    return -0.320 * (math.sqrt(egfr) - 8.8) \
           + 0.002 * (map - 97) \
           - 0.035 * (math.log(proteinuria) - 0.09) \
           + 0.004 * ((map * math.log(proteinuria)) - 8.3) \
           + 0.201 * mesangial \
           - .035 * endocapillary_hypercellilarity \
           + 0.084 * segmental_sclerosis \
           + 0.700 * t1 \
           + 1.237 * t2 \
           + 0.101 * t1 * math.log(proteinuria) \
           - 0.321 * t2 * math.log(proteinuria) \
           - 0.017 * (age - 38) \
           + 0.118 * rasb \
           + 0.166 * rasb * math.log(proteinuria) \
           - 0.266 * immunosuppression


def predict_risk(months, lp):
    return 1 - pow(baseline_survival(months), math.exp(lp))


def calculate_map(systoic_bp, diastoic_bp):
    return diastoic_bp + (systoic_bp - diastoic_bp) / 3


def baseline_survival(months):
    return 1.0003754 - 0.1131641 * pow((months + 0.1) / 100, 2) + 0.0964763 * pow((months + 0.1) / 100, 2) * math.log(
        (months + 0.1) / 100)
