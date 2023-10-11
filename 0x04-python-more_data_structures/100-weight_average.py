#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_tot = 0
    weight_tot = 0
    for i in my_list:
        score_tot = score_tot + (i[0] * i[1])
        weight_tot = weight_tot + i[-1]
    avg_weight = score_tot / weight_tot
    return avg_weight
