import pandas as pd
import numpy as np
def fill_data(path_excel_doc):
    df = pd.read_excel(path_excel_doc)
    a = []
    b = []
    for lines in df.values:
       a.append([lines[1],lines[2],lines[3]])
       b.append(lines[5])
    print('Исходные данные:')
    print(a)
    print(b)
    print()
    return [a,b]

def find_alfa_and_beta_and_A(a,b):
    matrA = np.array(a)
    matrV = np.array(b)
    matrE = np.array([[1,0,0],[0,1,0],[0,0,1]])
    rever_matrA = np.linalg.inv(matrE-matrA)
    resualt  = rever_matrA.dot(matrV)
    print('Результат:')
    print(resualt)

    return [resualt]

def potrep_A_B_C(a,b):
    x1,x2,x3 = 0 , 0 , 0
    x1 = np.sum(a[0])+b[0]
    x2 = np.sum(a[1])+b[1]
    x3 = np.sum(a[2])+b[2]
    k = []
    k1 = []
    k2 = []
    res = []
    for i in range(3):
        k.append(a[i][0]/x1)
        k1.append(a[i][1] / x2)
        k2.append(a[i][2] / x3)
        res.append([k[i], k1[i], k2[i]])

    print('A = \n' + str(res))
    return [res,[x1,x2,x3]]
print('Задание 1')
k = fill_data('data_for_task1.xlsx')
find_alfa_and_beta_and_A(k[0],k[1])
print('\nЗадание 2')
k = fill_data('data_for_task2.xlsx')
res = potrep_A_B_C(k[0],k[1])
find_alfa_and_beta_and_A(res[0],k[1])