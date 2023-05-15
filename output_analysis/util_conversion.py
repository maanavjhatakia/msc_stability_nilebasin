import pandas as pd
import numpy as np

#define functions for utility translation
def EgyptUtil(egypt_irr_BCM):
    #define variables for conversion
    n = 20 #number of years of simulation
    dv = 0.03 #discount value of 3% for calculating FV
    base_nile_allocation = 55.5 #BCM as per Nile agreement

    cost_egypt_barley = 0.28  #cost for major Egyptian crops (USD/kg)
    cost_egypt_corn = 0.3896
    cost_egypt_cotton = 0.2829
    cost_egypt_gn = 4.5242
    cost_egypt_soybeans = 0.3486
    cost_egypt_sorghum = 0.1823
    cost_egypt_wheat = 0.4202
    cost_egypt_sunflower = 0.5350
    cost_egypt_rice = 0.2204
    cost_egypt_list = [cost_egypt_barley, cost_egypt_corn, cost_egypt_cotton, cost_egypt_gn, cost_egypt_soybeans, cost_egypt_sorghum, 
                       cost_egypt_wheat, cost_egypt_rice]
    
    wu_egypt_barley = 0.4857  #water efficiency for each crop (m^3/m^2)
    wu_egypt_corn = 0.9081
    wu_egypt_cotton = 1.3312
    wu_egypt_gn = 0.9679
    wu_egypt_soybeans = 1.0083
    wu_egypt_sorghum = 0.9410
    wu_egypt_wheat = 0.6493
    wu_egypt_sunflower = 0.6726
    wu_egypt_rice = 1.2381
    wu_egypt_list = [wu_egypt_barley, wu_egypt_corn, wu_egypt_cotton, wu_egypt_gn, wu_egypt_soybeans, wu_egypt_sorghum,
                     wu_egypt_wheat, wu_egypt_rice]
    
    y_egypt_barley = 0.1179 #yield for each crop (kg/m^2)
    y_egypt_corn = 0.7257
    y_egypt_cotton = 0.0714
    y_egypt_gn = 0.2902
    y_egypt_soybeans = 0.2540
    y_egypt_sorghum = 0.4627
    y_egypt_wheat = 0.5806
    y_egypt_sunflower = 0.2177
    y_egypt_rice = 0.7620
    y_egypt_list = [y_egypt_barley, y_egypt_corn, y_egypt_cotton, y_egypt_gn, y_egypt_soybeans, y_egypt_sorghum,
                    y_egypt_wheat,y_egypt_rice]

    #calculations for finding water ratios
    #areas for cultivation (1000 ha)
    area_egypt_barley = 83
    area_egypt_corn = 836
    area_egypt_cotton = 96
    area_egypt_gn = 64
    area_egypt_soybeans = 9
    area_egypt_sorghum = 151
    area_egypt_wheat = 1360
    area_egypt_sunflower = 8
    area_egypt_rice = 637

    #water requirements based on average crop areas (m^3)
    wr_barley = ((area_egypt_barley) * 1e7)* wu_egypt_barley
    wr_corn = ((area_egypt_corn) * 1e7)* wu_egypt_corn
    wr_cotton = ((area_egypt_cotton) * 1e7) * wu_egypt_cotton
    wr_gn = ((area_egypt_gn)* 1e7) * wu_egypt_gn
    wr_soybeans = ((area_egypt_soybeans) * 1e7) * wu_egypt_soybeans
    wr_sorghum = ((area_egypt_sorghum) * 1e7) * wu_egypt_sorghum
    wr_wheat = ((area_egypt_wheat) * 1e7) * wu_egypt_wheat
    wr_sunflower = ((area_egypt_sunflower) * 1e7) * wu_egypt_sunflower
    wr_rice = ((area_egypt_rice) * 1e7) * wu_egypt_rice
    wr_list = [wr_barley,wr_corn,wr_cotton,wr_gn, wr_soybeans, wr_sorghum,wr_wheat, wr_rice]
    wr_sum = sum(wr_list)
    
    #ratios for theoretical water allocations for the deficit
    rat_barley = wr_barley / wr_sum
    rat_corn = wr_corn / wr_sum
    rat_cotton = wr_cotton / wr_sum
    rat_gn = wr_gn / wr_sum
    rat_soybeans = wr_soybeans / wr_sum
    rat_sorghum = wr_sorghum / wr_sum
    rat_wheat = wr_wheat / wr_sum
    #rat_sunflower = wr_sunflower / wr_sum
    rat_rice = wr_rice / wr_sum

    egypt_irr = (base_nile_allocation) * 0.8 * 1000000000 #bcm to m^3 conversion
    egypt_irr_wo_def = (base_nile_allocation * 0.8 - egypt_irr_BCM) * 1000000000
    egypt_irr_w_def = (base_nile_allocation * 0.8 + egypt_irr_BCM) * 1000000000

    #allocation amounts (m^3 or m^3/year)
    water_all_barley = egypt_irr_wo_def * rat_barley
    water_all_corn = egypt_irr_wo_def * rat_corn
    water_all_cotton = egypt_irr_wo_def * rat_cotton
    water_all_gn = egypt_irr_wo_def * rat_gn
    water_all_soybeans = egypt_irr_wo_def * rat_soybeans
    water_all_sorghum = egypt_irr_wo_def * rat_sorghum
    water_all_wheat = egypt_irr_wo_def * rat_wheat
   #water_all_sunflower = egypt_irr * rat_sunflower
    water_all_rice = egypt_irr_wo_def * rat_rice
    water_all_egypt_list = [water_all_barley, water_all_corn, water_all_cotton, water_all_gn, water_all_soybeans, water_all_sorghum,
                            water_all_wheat, water_all_rice]

    income_egypt_irr = []
    for i in range(len(water_all_egypt_list)):
        value = (water_all_egypt_list[i] * cost_egypt_list[i] * y_egypt_list[i] / wu_egypt_list[i]) * (1/(1 + dv) ** n) * (egypt_irr_wo_def / egypt_irr_w_def)
        income_egypt_irr.append(value)

    sum_income_egypt_irr = sum(income_egypt_irr)
    return sum_income_egypt_irr

    #egypt HAD levels 
def egypt_HAD_util(egypt_HAD):
    alpha = egypt_HAD #amount of time below min. hydropower production
    base_production_had = 10000 #GWh
    cost_hp_had = 0.10 #LCOE of electricity generation in Egypt per kWh
    n = 20 #number of years of simulation
    dv = 0.03 #discount value of 3% for calculating FV

    income_egypt_HAD = ((1-alpha) * base_production_had * 1000000 * cost_hp_had) * (1/(1 + dv) ** n)
    return income_egypt_HAD

def SudanUtil(sudan_irr_BCM):
    #define variables for conversion
    n = 20 #number of years of simulation
    dv = 0.03 #discount value of 3% for calculating FV
    base_nile_allocation_sud = 18.5 #BCM as per Nile agreement

    cost_sudan_cotton = 0.6173 #cost for major Sudanese crops (USD/kg)
    cost_sudan_gn = 0.6465
    cost_sudan_wheat = 0.7781
    cost_sudan_sorghum = 0.5646
    cost_sudan_list = [cost_sudan_cotton,cost_sudan_gn,cost_sudan_wheat,cost_sudan_sorghum]

    wu_sudan_cotton = 0.62 #water efficiency for each crop (m^3/m^2)
    wu_sudan_gn = 1.02
    wu_sudan_wheat = 0.355
    wu_sudan_sorghum = 0.815
    wu_sudan_list = [wu_sudan_cotton,wu_sudan_gn,wu_sudan_wheat,wu_sudan_sorghum]

    y_sudan_cotton = 0.0569 #yield of crops (kg/m^2)
    y_sudan_gn = 0.0725
    y_sudan_wheat = 0.2177
    y_sudan_sorghum = 0.0544
    y_sudan_list = [y_sudan_cotton,y_sudan_gn,y_sudan_wheat,y_sudan_sorghum]

    #calculations for finding water ratios
    #areas for cultivation (1000 ha)
    area_sudan_cotton = 192
    area_sudan_gn = 3109
    area_sudan_wheat = 269
    area_sudan_sorghum = 7460

    #water requirements based on average crop areas (m^3)
    wr_cotton = ((area_sudan_cotton) * 1e7) * wu_sudan_cotton
    wr_gn = ((area_sudan_gn) * 1e7) * wu_sudan_gn
    wr_wheat = ((area_sudan_wheat) * 1e7) * wu_sudan_wheat
    wr_sorghum = ((area_sudan_sorghum) * 1e7) * wu_sudan_sorghum
    wr_list = [wr_cotton,wr_gn,wr_wheat,wr_sorghum]
    wr_sum = sum(wr_list)

    #theoretical water allocations ratios
    rat_cotton = wr_cotton / wr_sum
    rat_gn = wr_gn / wr_sum
    rat_wheat = wr_wheat / wr_sum 
    rat_sorghum = wr_sorghum / wr_sum 

    sudan_irr = (base_nile_allocation_sud) * 1000000000 #bcm to m^3 conversion
    sudan_irr_wo_def = (base_nile_allocation_sud - sudan_irr_BCM) * 1000000000
    sudan_irr_w_def = (base_nile_allocation_sud + sudan_irr_BCM) * 1000000000

    #allocation amounts (m^3 or m^3/year)
    water_all_cotton = sudan_irr * rat_cotton
    water_all_gn = sudan_irr * rat_gn
    water_all_wheat = sudan_irr * rat_wheat
    water_all_sorghum = sudan_irr * rat_sorghum
    water_all_sudan_list = [water_all_cotton,water_all_gn,water_all_wheat,water_all_sorghum]

    income_sudan_irr = []
    for i in range(len(water_all_sudan_list)):
        value = (sudan_irr_wo_def / sudan_irr_w_def) * (water_all_sudan_list[i] * cost_sudan_list[i] * y_sudan_list[i] / wu_sudan_list[i]) * (1/(1 + dv) ** n)
        income_sudan_irr.append(value)

    sum_income_sudan_irr = sum(income_sudan_irr)
    return sum_income_sudan_irr

def EthUtil(hp_gerd):
    #define variables for conversion
    n = 20 #number of years of simulation
    dv = 0.03 #discount value of 3% for calculating FV

    cost_export = 0.10 # per kWh
    pc_export = 0.12 
    cost_domestic = 0.05 #per kWh
    pc_domestic_use = 1 - pc_export
    hp_gerd_kWh = hp_gerd / (1e-9)

    hp_income_gerd = (1 / (1 + dv) ** n) * ((pc_export * hp_gerd_kWh * cost_export) + 
                                                pc_domestic_use * hp_gerd_kWh * cost_domestic)
    
    return hp_income_gerd