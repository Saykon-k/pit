import copy
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
    dict_info_mini_t = {}
    dict_info_big_T = {}
    k = 0
    for i in ranked_info.values():
        prom_info = []
        for j in i:
            if connection_from_user[j][0] == -1:
                dict_info_mini_t[f't_{k}'] = info_about_work[j]
                dict_info_big_T[f'T_{k}'] = info_about_work[j]
                k +=1
            else:
                dict_info_mini_t[f't_{k}'] = info_about_work[j]
                prom_list = [dict_info_big_T.get(f'T_{i}') for i in connection_from_user[j]]
                # # for i in connection_from_user:
                # if f'T_{k}' == 'T_11':
                #     print('------')
                #     print(dict_info_mini_t)
                #     print(connection_from_user[j])
                #     print(prom_list)
                #     print('------')
                dict_info_big_T[f'T_{k}'] = info_about_work[j] + max(prom_list)
                prom_info.append(max([info_about_work[i] for i in connection_from_user[j]]) + info_about_work[j])
                k += 1
        prom_info_date.append(copy.deepcopy(prom_info))
        prom_info.clear()
    # print(dict_info_big_T)
    # print(dict_info_mini_t)
    return [dict_info_mini_t, dict_info_big_T]

def find_max_path(connection_from_user, info_about_T, info_):
    max_path = -1
    key_max = -1
    for i, j in info_about_t_and_T.items():
        if j > max_path:
            max_path = j
            key_max = i
    print(key_max)

def main(connection_from_user, info_about_work):
    ranked_info = determite_work(connection_from_user)
    print('find_max_path')
    info_about_t_and_T = find_t_and_T(connection_from_user, ranked_info, info_about_work)
    find_max_path(connection_from_user, info_about_t_and_T)


# main([[-1],[0,2],[-1],[0,1,2],[-1],[-1],[0,3,9],[0,1],[2,3,4],[8],[6,11],[0,1],[3,4,9],[2,3,4],[9],[6]],
#                [10, 5, 15, 10, 30, 5, 15, 25, 15, 30, 35, 10])
main([[-1], [-1], [-1], [0, 1], [1, 2], [1, 3], [2, 4], [3, 4], [6], [5, 7], [8, 9], [9]],
     [10, 5, 15, 10, 30, 5, 15, 25, 15, 30, 35, 10])
