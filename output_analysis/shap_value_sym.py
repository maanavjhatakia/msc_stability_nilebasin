import math

def shapleyval_sym(list1, list2, player_code):
    merged_list = [(list1[i],list2[i]) for i in range(0,len(list1))] #create tuple with the list1 and list2 values
    ind_solutions = []
    n = 3

    #divide relevant coalitions based on interested player
    if player_code == 1:
        player = 'Egypt'

        #divide based on temporary lists with coalitions with(out) the specific player
        temp_coalition_list_eg = [] 
        temp_coalition_list_with_eg = []
        temp_char_function_list_eg = []
        temp_char_function_list_with_eg = []

        #for each value in the merged list of coalitions/characteristic functions above
        for val in merged_list: #check if the coalition is relevant to the player
            if player not in val[0]:
                temp_coalition_list_eg.append(val[0])
                temp_char_function_list_eg.append(val[1])
            elif player in val[0]:
                temp_coalition_list_with_eg.append(val[0])
                temp_char_function_list_with_eg.append(val[1])
        
        s_value = []
        for item in temp_coalition_list_with_eg:
            s = len(item.split()) - 1
            s_value.append(s)

        for j in range(len(temp_coalition_list_eg)): #for each value in the lists 
            shap_ind_val = math.factorial(s_value[j]) * math.factorial(n - 1 - s_value[j]) * (temp_char_function_list_with_eg[j]
                                                                      - temp_char_function_list_eg[j])
            ind_solutions.append(shap_ind_val)

    elif player_code == 2:
        player = 'Sudan'
        temp_coalition_list_su = []
        temp_coalition_list_with_su = []
        temp_char_function_list_su = []
        temp_char_function_list_with_su = []
        for val in merged_list:
            if player not in val[0]:
                temp_coalition_list_su.append(val[0])
                temp_char_function_list_su.append(val[1])
            elif player in val[0]:
                temp_coalition_list_with_su.append(val[0])
                temp_char_function_list_with_su.append(val[1])
        
        s_value = []
        for item in temp_coalition_list_with_su:
            s = len(item.split()) - 1
            s_value.append(s)

        for j in range(len(temp_coalition_list_su)):
            shap_ind_val = math.factorial(s_value[j]) * math.factorial(n - 1 - s_value[j]) * (temp_char_function_list_with_su[j]
                                                                      - temp_char_function_list_su[j])
            ind_solutions.append(shap_ind_val)   

    elif player_code == 3:
        player = 'Ethiopia'
        temp_coalition_list_et = []
        temp_coalition_list_with_et = []
        temp_char_function_list_et = []
        temp_char_function_list_with_et = []
        for val in merged_list:
            if player not in val[0]:
                temp_coalition_list_et.append(val[0])
                temp_char_function_list_et.append(val[1])
            elif player in val[0]:
                temp_coalition_list_with_et.append(val[0])
                temp_char_function_list_with_et.append(val[1])

        s_value = []
        for item in temp_coalition_list_with_et:
            s = len(item.split()) - 1
            s_value.append(s)

        for j in range(len(temp_coalition_list_et)):
            shap_ind_val = math.factorial(s_value[j]) * math.factorial(n - 1 - s_value[j]) * (temp_char_function_list_with_et[j]
                                                                      - temp_char_function_list_et[j])
            ind_solutions.append(shap_ind_val)

    shap_val = sum(ind_solutions) * (1/ math.factorial(n))
    return shap_val