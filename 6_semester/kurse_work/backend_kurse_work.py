import copy
import cvxpy as cp
import numpy as np
import math
# кароч 1 связи, которые проставил пользователь ниже функция пример
# выходной список - список индексов, по которым нужно будет строить граф - учебник фрола - сошлось - ок
def determite_work(connection_from_user):
    rank_table = []
    print(connection_from_user)
    data_info = list(range(len(connection_from_user)))
    data_info.insert(0,-1)
    info_about_rank = {-1: set()}
    not_none_index = []
    for i in range(len(connection_from_user)):
        if len(connection_from_user[i]) == 1 and connection_from_user[i][0] == -1:
            info_about_rank.get(-1).add(i)
        else:
            not_none_index.append(i)
    print([connection_from_user[i] for i in not_none_index])

    # print(not_none_index)
    set_insected = set()
    prom = []
    print(not_none_index)
    while len(not_none_index) != 0:
        for i in not_none_index:
            last_rank = -20
            check_index_valide = 0
            for j in connection_from_user[i]:
                for i1, i2 in info_about_rank.items():
                    if j in i2:
                        check_index_valide += 1
                        if last_rank < i1:
                            last_rank = i1

            if check_index_valide == len(connection_from_user[i]):
                # print(connection_from_user[i])
                # print(i)
                if not last_rank + 1 in info_about_rank.keys():
                    info_about_rank[last_rank + 1] = set()
                    info_about_rank.get(last_rank + 1).add(i)
                else:
                    info_about_rank.get(last_rank + 1).add(i)
            else:
                prom.append(i)
            # print('----')

            # print(info_about_rank)
                # print(last_rank)
                # print(j)
                # print()
        # print(info_about_rank)

        not_none_index = copy.deepcopy(prom)
        prom = []
    for i1, i in info_about_rank.items():
        print(i1, '->', i)
    return info_about_rank

def find_t_and_T(connection_from_user, ranked_info, info_about_work):
    prom_info_date = []
    dict_info_t = {}
    k = 0
    for i in ranked_info.values():
        prom_info = []
        for j in i:
            if connection_from_user[j][0] == -1:
                dict_info_t[f't_{j}'] = info_about_work[j]
                dict_info_t[f'T_{j}'] = info_about_work[j]
                k += 1
            else:
                # print('---------')
                # print(i)
                # print(j)
                # print(dict_info_t)
                # print(connection_from_user[j])
                dict_info_t[f't_{k}'] = info_about_work[j]
                prom_list = [dict_info_t.get(f'T_{i}') for i in connection_from_user[j]]
                # print('---------')

                # # for i in connection_from_user:
                # if f'T_{k}' == 'T_11':
                #     print('------')
                #     print(dict_info_mini_t)
                #     print(connection_from_user[j])
                #     print(prom_list)
                #     print('------')
                dict_info_t[f'T_{j}'] = info_about_work[j] + max(prom_list)
                k += 1
        prom_info_date.append(copy.deepcopy(prom_info))
        prom_info.clear()
    # print(dict_info_big_T)
    # print(dict_info_mini_t)
    print(dict_info_t)
    return dict_info_t

def find_max_key(info_about_T):
    max_path = -1
    key_max = -1
    for i, j in info_about_T.items():
        if j > max_path:
            max_path = j
            key_max = i
    return key_max

def find_max_path(connection_from_user, info_about_T):
   key_max = find_max_key(info_about_T)
   value_to_next = int(key_max.split('_')[1])
   prom_path = [value_to_next]

   while connection_from_user[value_to_next][0] != -1:
        prom = [[i, info_about_T.get(f'T_{i}')] for i in connection_from_user[value_to_next]]
        max_element = -1
        number_info = -1
        for i in prom:
            if i[1] > max_element:
                max_element = i[1]
                number_info = i[0]
        prom_path.append(number_info)
        value_to_next = number_info

   return prom_path
   #      print('-----')
   #      print(connection_from_user[value_to_next])
   #
   #      print('-----')
   #
   # print(prom_path)
from math import ceil, floor
def opt_v1_without_change_path(connection_from_user, ranked_info, info_about_work,info_about_faster_work, max_path, alfa, money, max_user_time):
    dict_values = {}
    # x = cp.Variable()
    print(max_path)
    constraints = []
    for i in max_path:
        dict_values[f'x_{i}'] = cp.Variable()

        constraints.append(info_about_work[i]*(1-alfa[i]*dict_values.get(f'x_{i}'))>= info_about_faster_work[i])

    # constraints = [x  < 10]

    # constraints = [dict_values.get(f'x_{7}')]
    # print(constraints)
    # # print(alfa)
    # print([info_about_work[i] for i in max_path])
    # # print([dict_values.get(f'x_{i}') * 1 < 10 for i in max_path])
    #
    constraints.append(sum([info_about_work[i]*(1-alfa[i]*dict_values.get(f'x_{i}')) for i in max_path]) <= max_user_time)
    constraints.append(sum([ dict_values.get(f'x_{i}') for i in max_path]) <= money)

    for i in max_path:
        constraints.append(dict_values.get(f'x_{i}') >= 0)
    # print('\ncontains')
    # for i in range(len(constraints)):
    #
    #     print(str(constraints[i]))
    # print('contains\n')

    # for i in max_path:
    #     prom =
    #
    obj = cp.Minimize(sum([dict_values.get(f'x_{i}') for i in max_path]))
    #
    prob = cp.Problem(obj, constraints)
    #
    prob.solve()
    print("status:", prob.status)
    if str(prob.status) == 'optimal':
        print("optimal val:", np.round(prob.value, 5))

        for i in max_path:
            print("optimal var {0}: (floor){1}\n".format( f'x_{i}', round(float(dict_values.get(f'x_{i}').value), 3)))
            # print(np.round(dict_values.get(f'x_{i}').value),3)

            # float_round(0.21111, 3, round)
            print(round(info_about_work[i] * (1 - alfa[i] * dict_values.get(f'x_{i}').value),2))

    else:
        print('tet')
        return -404
def opt_v2_max_mathematic_model(connection_from_user, ranked_info,
                                info_about_work,info_about_faster_work,
                                max_path, alfa, money,
                                max_user_time,info_about_t_and_T):

    dict_values = {}
    # x = cp.Variable()
    print(ranked_info)
    constraints = []
    for i in range(len(connection_from_user)):
        dict_values[f'x_{i}'] = cp.Variable()
        constraints.append(info_about_work[i]*(1-alfa[i]*dict_values.get(f'x_{i}')) >= info_about_faster_work[i])
    k = 0
    print('\ncontains')
    for i in range(len(constraints)):
        print(str(constraints[i]))
        k+=1
    print('contains\n')
    for i, j in ranked_info.items():
        if i == -1:
            pass
            # for i_1 in ranked_info.get(i):
            #     constraints.append(info_about_work[i_1]*(1-alfa[i_1]*dict_values.get(f'x_{i_1}')) == info_about_t_and_T.get(f'T_{i_1}'))
        else:
            for i_1 in ranked_info.get(i):
                for i_2 in connection_from_user[i_1]:
                    print(i_2)
                    # constraints.append(info_about_t_and_T.get(f't_{i_1}'))

                    # constraints.append(ranked_info[i_2]*(1-alfa[i_2]))
                    if i == 0:
                        constraints.append(info_about_t_and_T.get(f'T_{i_1}') - info_about_work[i_1] >=
                                           info_about_work[i_2]*(1-alfa[i_2]*dict_values.get(f'x_{i_2}')))
                    else:
                        constraints.append(info_about_t_and_T.get(f'T_{i_1}') - info_about_work[i_1] >=
                                           (info_about_t_and_T.get(f'T_{i_2}') - info_about_work[i_2]) + info_about_work[i_2]*(1-alfa[i_2]*dict_values.get(f'x_{i_2}')))

    print('\ncontains-1')
    for i in constraints[k:]:
        print(str(i))
        k += 1
    print('contains\n')
    #
    print(max_user_time)
    for i in range(0, len(connection_from_user)-3, 1):
        constraints.append(max_user_time >= (info_about_t_and_T.get(f'T_{i}') - info_about_work[i]) + info_about_work[i]*(1-alfa[i]*dict_values.get(f'x_{i}')))



    print('\ncontains - 2 ')
    for i in constraints[k:]:
        print(str(i))
        k += 1
    print('contains\n')
    for i in range(len(connection_from_user)):
        constraints.append(dict_values.get(f'x_{i}') >= 0)
    #
    #
    constraints.append(sum(list(dict_values.values())) <= money)

    # print('contains\n')
    # print(constraints[-1])


    # print('\ncontains')
    # for i in range(len(constraints)):
    #
    #     print(str(constraints[i]))
    # print('contains\n')
    # for i in range(len(connection_from_user)):
    #     constraints.append(dict_values.get(f'x_{i}') == 0)
        # print(sum([dict_values.get(f'x_{i}') for i in range(len(connection_from_user))]))

    obj = cp.Minimize(sum([dict_values.get(f'x_{i}') for i in range(len(connection_from_user))]))

    # obj = cp.Maximize(sum([dict_values.get(f'x_{i}') for i in range(len(connection_from_user[4:]))]))

    #
    prob = cp.Problem(obj, constraints)
    #
    prob.solve()
    print("status:", prob.status)
    print("optimal val:", np.round(prob.value, 5))
    k = 0
    for i in range(len(connection_from_user)):
        print(f'x_{i}', round(float(dict_values.get(f'x_{i}').value),3))
        k += dict_values.get(f'x_{i}').value
    print(k)
    print()
    obj = cp.Maximize(sum([dict_values.get(f'x_{i}') for i in range(len(connection_from_user))]))

    prob = cp.Problem(obj, constraints)
    #
    prob.solve()
    print("status:", prob.status)
    print("optimal val:", np.round(prob.value, 5))
    k = 0
    for i in range(len(connection_from_user)):
        print(f'x_{i}',  round(float(dict_values.get(f'x_{i}').value),3))
        k += dict_values.get(f'x_{i}').value
    print(k)
        # print("optimal var {0}: (floor){1}\n".format(f'x_{i}', dict_values.get(f'x_{i}').value))
        # print(np.round(dict_values.get(f'x_{i}').value),3)

        # float_round(0.21111, 3, round)
        # print(round(info_about_work[i] * (1 - alfa[i] * dict_values.get(f'x_{i}').value), 2))

    # for i in range(len(constraints)):
    #     print(constraints[i])
    #     print()
    # print('contains\n')


        # dict_values[f'x_{i}'] = cp.Variable()
        # constraints.append(info_about_work[i] * (1 - alfa[i] * dict_values.get(f'x_{i}')) >= info_about_faster_work[i])

def main(connection_from_user, info_about_work, info_about_faster_work, alfa, money, max_user_time):
    ranked_info = determite_work(connection_from_user)
    print('info_about_t_and_T')
    info_about_t_and_T = find_t_and_T(connection_from_user, ranked_info, info_about_work)
    print('find_max_path')
    max_path = find_max_path(connection_from_user, info_about_t_and_T)
    opt_v1_without_change_path(connection_from_user, ranked_info, info_about_work, info_about_faster_work, max_path, alfa, money, max_user_time)
    opt_v2_max_mathematic_model(connection_from_user, ranked_info, info_about_work, info_about_faster_work, max_path, alfa, money, max_user_time, info_about_t_and_T)

# пример из начала - то, что он дает на первом методе - ок (не было еще параметров)
# main([[-1], [-1], [-1], [0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [6], [5, 7], [8, 9], [9]],
#      [10, 5, 15, 10, 30, 5, 15, 25, 15, 30, 35, 10],
#      [15, 5, 5, 10, 5, 10, 3, 5],
#           [0.1, 0.15, 0.1, 0.2, 0.2, 0.01, 0.05, 0.1],
#           60,
#           32
#      )
#да.
# main([[-1],[-1],[-1],[0],[0],[2],[1, 4, 5], [1, 4, 5],[3, 6], [2], [1, 3, 5,9]],
#      [8, 10, 6, 9, 5, 2, 4, 13, 8, 17, 10])
# main([[-1],[-1],[-1],[0,1],[0,1,2],[0,1,2],[5],[3,4,6]],
#      [20, 10, 5, 30, 10, 15, 10, 10],
#      [15, 5, 5, 10, 5, 10, 3, 3],
#      [0.1, 0.15, 0.1, 0.2, 0.2, 0.01, 0.05, 0.1],
#      10,
#      35)
main([[-1],[-1],[-1],[0,1],[0,1,2],[0,1,2],[5],[3,4,6]],
     [20, 10, 5, 30, 10, 15, 10, 10],
     [15, 5, 5, 10, 5, 10, 3, 3],
     [0.1, 0.15, 0.1, 0.2, 0.2, 0.01, 0.05, 0.1],
     60,
     32)