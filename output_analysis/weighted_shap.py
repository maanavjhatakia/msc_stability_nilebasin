import pandas as pd 
import math 
import numpy as np 

def shapleyval_asym(list1, list2, player_code,list_weights):
    merged_list = [(list1[i],list2[i]) for i in range(0,len(list1))] #create tuple with the list1 and list2 values
    ind_solutions = []
    n = 3

    if player_code == 1: 
        player = "Egypt"
        temp_coalition_list_wo_eg = [] #set up the temporary lists needed to separate relevant coalitions
        temp_coalition_list_w_eg = [] #same as above, but for characteristic function values
        temp_charfunc_list_wo_eg = []
        temp_charfunc_list_w_eg = []

        for val in merged_list:
            if player not in val[0]:
                temp_coalition_list_wo_eg.append(val[0])
                temp_charfunc_list_wo_eg.append(val[1])
            elif player in val[0]:
                temp_coalition_list_w_eg.append(val[0])
                temp_charfunc_list_w_eg.append(val[1])

        for i in range(len(temp_coalition_list_w_eg)):
            shap_val = list_weights[i] * (temp_charfunc_list_w_eg[i] - temp_charfunc_list_wo_eg[i])
            ind_solutions.append(shap_val)

    elif player_code == 2:
        player = "Sudan"
        temp_coalition_list_wo_su = []
        temp_coalition_list_w_su = []
        temp_charfunc_list_wo_su = []
        temp_charfunc_list_w_su = []

        for val in merged_list:
            if player not in val[0]:
                temp_coalition_list_wo_su.append(val[0])
                temp_charfunc_list_wo_su.append(val[1])
            elif player in val[0]:
                temp_coalition_list_w_su.append(val[0])
                temp_charfunc_list_w_su.append(val[1])
        
        for i in range(len(temp_coalition_list_w_su)):
            shap_val = list_weights[i] * (temp_charfunc_list_w_su[i] - temp_charfunc_list_wo_su[i])
            ind_solutions.append(shap_val)

    elif player_code == 3: 
        player = "Ethiopia"
        temp_coalition_list_wo_et = []
        temp_coalition_list_w_et = []
        temp_charfunc_list_wo_et = []
        temp_charfunc_list_w_et = []

        for val in merged_list:
            if player not in val[0]:
                temp_coalition_list_wo_et.append(val[0])
                temp_charfunc_list_wo_et.append(val[1])
            elif player in val[0]:
                temp_coalition_list_w_et.append(val[0])
                temp_charfunc_list_w_et.append(val[1])

        for i in range(len(temp_coalition_list_w_et)):
            shap_val = list_weights[i] * (temp_charfunc_list_w_et[i] - temp_charfunc_list_wo_et[i])
            ind_solutions.append(shap_val)

    weighted_shap_val = sum(ind_solutions)
    return weighted_shap_val