import pandas as pd
import numpy as np
def fill_data(path_excel_doc):
    df = pd.read_excel(path_excel_doc)
    log_gpd_sum, log_k_l_del, log_l_sum, log_k_2_sum = 0, 0, 0, 0
    log_k_l_y_del_2, log_l_k_sum, log_k_l_del_2, log_y_l_del = 0, 0, 0, 0

    for lines in df.values[1:]:
        prom_y = lines[1]
        prom_k = lines[2]
        prom_l = lines[3]
        log_k_l_del += np.log(prom_k/prom_l)
        log_y_l_del += np.log(prom_y/prom_l)
        log_k_l_del_2 += np.log(prom_k/prom_l)**2
        log_k_l_y_del_2 += np.log(prom_k/prom_l)*np.log(prom_y/prom_l)
    return [log_k_l_del,  log_y_l_del,log_k_l_del_2,log_k_l_y_del_2]

def find_alfa_and_beta_and_A(data_coverted):

    matrA = np.array([[15,data_coverted[0]],
                      [data_converted[0],data_converted[2]]])
    matrV = np.array([[data_converted[1]],
                      [data_converted[3]]])
    print(str(matrA)+" = " + str(matrV) )

    rever_matrA = np.linalg.inv(matrA)
    resualt  = rever_matrA.dot(matrV)

    print(rever_matrA)
    print()
    print(matrV)
    print()
    A = resualt[0]
    alfa = resualt[1]
    print('a ' + str(A))
    #print(np.exp(A))
    print('alfa ' + str(alfa))

    return [A,alfa]
data_converted = fill_data('data_usa.xls')
find_alfa_and_beta_and_A(data_converted)
