from datetime import datetime
import time
def countS(num):
    return int(str(num*num)[-len(str(num))::]) == num
def countSN(num):
    a = len(str(num * num))
    print(a)
    return str(num*num)[-len(str(num))::] == str(num)
def countN(num):
    return (num * num) % pow(10, countlen(num)) == num;

def countlen(num):
    ket = 0;
    while ((num) != 0):
        num = num // 10
        ket+=1
    return ket;
    return str(num*num)[-len(str(num)):] == str(num)
def is_animorph(number):
    string_number = str(number)
    length_number = len(string_number)
    square = number*number
    string_square = str(square)

    return string_square[-length_number::] == string_number
print(countSN(12_890_625))
# col_digit = 50_000_000
# start_time = datetime.now()
# for i in range(col_digit):
#     countS(i)
# print("время работы функции countS")
# print(datetime.now() - start_time)
#
# start_time = datetime.now()
# for i in range(col_digit):
#     countSN(i)
# print("время работы функции countSN")
# print(datetime.now() - start_time)
#
# start_time = datetime.now()
# for i in range(col_digit):
#     countN(i)
# print("время работы функции countN")
# print(datetime.now() - start_time)
#
#
# start_time = datetime.now()
# for i in range(col_digit):
#     is_animorph(i)
# print("время работы функции is_animorph")
# print(datetime.now() - start_time)



