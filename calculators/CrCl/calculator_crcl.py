def calculate(age, weight, serum, gender):
    crcl_score = (140-age) * weight / (serum*72)
    if gender == 'female':
        crcl_score = crcl_score * .85

    return crcl_score


