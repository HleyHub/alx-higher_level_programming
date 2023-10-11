#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    for score, weight in my_list:
        score_tot = score * weight
        weight_tot = weight + weight
    if weight_tot == 0:
        return 0
    avg_weight = score_tot / weight_tot
    return avg_weight
