import math



def calculate_morbidity(physiological_score, operative_score):

    # This is based on the POSSUM equation
    x = -5.91 + (0.16 * physiological_score) + (0.19 * operative_score)
    morbidity_risk = 1 / (1 + math.exp(-1 * x))

    return round(morbidity_risk * 100,1)


def calculate_mortality(physiological_score, operative_score):

    # This is based on the P-POSSUM equation
    x = -9.065 + (0.1692 * physiological_score) + (0.155 * operative_score)
    mortality_risk = 1 / (1 + math.exp(-1 * x))

    return round(mortality_risk * 100,1)


def cal_physiological_score(age, cardiac_signs, respiratory_signs, systolic_bp, pulse, glasgow_coma_score,
                            urea_nitrogen, sodium, potassium, haemoglobin, wcc, electrocardiogram, NMPI):
    ps = 0


    if age == '&#60; 61':
        ps += 1
    elif age == '61 - 70':
        ps += 2
    elif age == '&#62; 70':
        ps += 4
    else:
        print('age error',age, NMPI)

    if cardiac_signs == 'No failure, normal CXR':
        ps += 1
    elif cardiac_signs == 'Antihypertensives, antianginals, digoxin, diuretics, no cardiomegally':
        ps += 2
    elif cardiac_signs == 'Peripheral oedema, warfarin, borderline cardiomegaly':
        ps += 4
    elif cardiac_signs == 'Raised JVP, cardiomegaly':
        ps += 8
    else:
        print('cardiac signs error',cardiac_signs, NMPI)

    if respiratory_signs == 'No dyspnoea':
        ps += 1
    elif respiratory_signs == 'Dyspnoea on exertion, mild COPD':
        ps += 2
    elif respiratory_signs == 'Limiting dyspnoea, moderate COPD':
        ps += 4
    elif respiratory_signs == 'Dyspnoea at rest, pulmonary fibrosis or consolidation on CXR':
        ps += 8
    else:
        print('resp error',respiratory_signs, NMPI)

    if systolic_bp == '110 - 130':
        ps += 1
    elif systolic_bp == '131 - 170' or systolic_bp == '100 - 109':
        ps += 2
    elif systolic_bp == '&#62; 170' or systolic_bp == '90 - 99':
        ps += 4
    elif systolic_bp == '&#60; 90':
        ps += 8
    else:
        print('systolic bp error',systolic_bp, NMPI)

    if pulse == '50 - 80':
        ps += 1
    elif pulse == '81 - 100' or pulse == '40 - 49':
        ps += 2
    elif pulse == '101 - 120':
        ps += 4
    elif pulse == '&#62; 120' or pulse == '&#60; 40':
        ps += 8
    else:
        print('pulse error', pulse, NMPI)

    if urea_nitrogen < 7.5:
        ps += 1
    elif 7.5 <= urea_nitrogen < 10:
        ps += 2
    elif 10 <= urea_nitrogen < 15:
        ps += 4
    elif 15 <= urea_nitrogen:
        ps += 8
    else:
        print('urea nitrogen error', urea_nitrogen, NMPI)

    if sodium > 135:
        ps += 1
    elif 130 < sodium <= 135:
        ps += 2
    elif 126 <= sodium <= 130:
        ps += 4
    elif sodium < 126:
        ps += 8
    else:
        print('sodium error', sodium, NMPI)

    if 3.4 < potassium < 5.1:
        ps += 1
    elif 3.1 < potassium <= 3.4 or 5.1 <= potassium < 5.4:
        ps += 2
    elif 2.9 <= potassium <= 3.1 or 5.4 <= potassium <= 5.9:
        ps += 4
    elif potassium < 2.9 or potassium > 5.9:
        ps += 8
    else:
        print('potassium error', potassium, NMPI)

    if glasgow_coma_score == '15':
        ps += 1
    elif glasgow_coma_score == '12 - 14':
        ps += 2
    elif glasgow_coma_score == '9 - 11':
        ps += 4
    elif glasgow_coma_score == '&#60; 9':
        ps += 8
    else:
        print('glassgow coma score error',glasgow_coma_score, NMPI)

    if 4 < wcc < 10.1:
        ps += 1
    elif 10.1 <= wcc <= 20 or 3 <= wcc <= 4:
        ps += 2
    elif wcc > 20 or wcc < 3:
        ps += 4
    else:
        print('wcc error', wcc, NMPI)

    if electrocardiogram == 'Normal':
        ps += 1
    elif electrocardiogram == 'AF, rate 60-90':
        ps += 4
    elif electrocardiogram == 'Other abnormal rhythmn, &#62;4&#47;min ectopics, Q waves, ST&#47;T changes':
        ps += 8
    else:
        print('ecg error',electrocardiogram, NMPI)

    if 129 < haemoglobin <= 160:
        ps += 1
    elif 114 < haemoglobin <= 129 or 160 < haemoglobin <= 170:
        ps += 2
    elif 100 <= haemoglobin <= 114 or 170 < haemoglobin <= 180:
        ps += 4
    elif haemoglobin < 100 or haemoglobin > 180:
        ps += 8
    else:
        print('haemoglobin error', haemoglobin, NMPI)

    return ps


def cal_operative_score(operative_magnitude, no_of_operations, blood_loss_per_operation, peritoneal_contamination,
                        presence_of_malignancy, timing_of_operation):
    os = 0

    if operative_magnitude == 'Minor':
        os += 1
    elif operative_magnitude == 'Moderate':
        os += 2
    elif operative_magnitude == 'Major':
        os += 4
    elif operative_magnitude == 'Complex Major':
        os += 8

    if no_of_operations == '1':  # check the code there is disruption
        os += 1
    elif no_of_operations == '2':
        os += 4
    elif no_of_operations == '&#62; 2':
        os += 8

    if blood_loss_per_operation == '&#60; 100':
        os += 1
    elif blood_loss_per_operation == '101 - 500':
        os += 2
    elif blood_loss_per_operation == '501 - 999':
        os += 4
    elif blood_loss_per_operation == '&#62; 1000':
        os += 8

    if peritoneal_contamination == 'No soiling':
        os += 1
    elif peritoneal_contamination == 'Minor soiling':
        os += 2
    elif peritoneal_contamination == 'Local pus':
        os += 4
    elif peritoneal_contamination == 'Free bowel content, pus, or blood':
        os += 8

    if presence_of_malignancy == 'None':
        os += 1
    elif presence_of_malignancy == 'Primary only':
        os += 2
    elif presence_of_malignancy == 'Nodal metastases':
        os += 4
    elif presence_of_malignancy == 'Distant metastases':
        os += 8

    if timing_of_operation == 'Elective':
        os += 1
    elif timing_of_operation == 'Urgent &#40;2 - 24 hrs&#41;':
        os += 4
    elif timing_of_operation == 'Emergency &#40; &#60; 2 hrs&#41;':
        os += 8

    return os
