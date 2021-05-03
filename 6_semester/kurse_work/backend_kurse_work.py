import copy
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
                print(connection_from_user[i])
                print(i)
                if not last_rank + 1 in info_about_rank.keys():
                    info_about_rank[last_rank + 1] = set()
                    info_about_rank.get(last_rank + 1).add(i)
                else:
                    info_about_rank.get(last_rank + 1).add(i)
            else:
                prom.append(i)
            print('----')

            # print(info_about_rank)
                # print(last_rank)
                # print(j)
                # print()
        # print(info_about_rank)
        for i1,i in info_about_rank.items():
            print(i1, '->', i)
        not_none_index = copy.deepcopy(prom)
        prom = []


determite_work([[-1],[0,2],[-1],[0,1,2],[-1],[-1],[0,3,9],[0,1],[2,3,4],[8],[6,11],[0,1],[3,4,9],[2,3,4],[9],[6]])
# a  = 1
# print(a)