import pandas as pd
import numpy as np
import sympy as sym

def fill_data(path_excel_doc):
    df = pd.read_excel(path_excel_doc)
    log_gpd_sum, log_k_sum, log_l_sum, log_k_2_sum = 0, 0, 0, 0
    log_l_2_sum, log_l_k_sum, log_k_gdp_sum, log_l_gdp_sum = 0, 0, 0, 0

    for lines in df.values[1:]:
        prom_log_gpd = np.log(lines[1])
        prom_log_k = np.log(lines[2])
        prom_log_l = np.log(lines[3])
        log_gpd_sum += prom_log_gpd
        log_k_sum += prom_log_k
        log_l_sum += prom_log_l
        log_k_2_sum += (prom_log_k*prom_log_k)
        log_l_2_sum+= (prom_log_l*prom_log_l)
        log_l_k_sum += (prom_log_l*prom_log_k)
        log_k_gdp_sum += (prom_log_k*prom_log_gpd)
        log_l_gdp_sum += (prom_log_l*prom_log_gpd)

    return [log_gpd_sum, log_k_sum, log_l_sum, log_k_2_sum, log_l_2_sum, log_l_k_sum, log_k_gdp_sum, log_l_gdp_sum]

def find_alfa_and_beta_and_A(data_coverted):
    log_gpd_sum, log_k_sum, log_l_sum, log_k_2_sum = data_coverted[0], data_converted[1], data_converted[2], data_converted[3]
    log_l_2_sum, log_l_k_sum, log_k_gdp_sum, log_l_gdp_sum = data_converted[4], data_converted[5], data_converted[6], data_converted[7]

    matrA = np.array([[15,log_k_sum,log_l_sum],
                      [log_k_sum,log_k_2_sum,log_l_k_sum],
                      [log_l_sum,log_l_k_sum,log_l_2_sum]])
    matrV = np.array([[log_gpd_sum],
                      [log_k_gdp_sum],
                      [log_l_gdp_sum]])

    rever_matrA = np.linalg.inv(matrA)
    resualt  = rever_matrA.dot(matrV)

    A = resualt[0]
    alfa = resualt[1]
    beta = resualt[2]
    print(resualt)
    return [A,alfa,beta]

data_converted = fill_data('data_usa.xls')
find_alfa_and_beta_and_A(data_converted)