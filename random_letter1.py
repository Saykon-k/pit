import random
l = ['весна','самовар','лето']
l1 = random.randint(0,2)
e = l[l1]
l1 = random.randint(0,2)
e1 = e[l1]
print(e[:e.index(e1)]+'?'+e[e.index(e1)+1:])
a = input()
if a == e1 :
    print('вы-молодцы!')
else:
    print('НЕ ОТЧАИВАЙТЕСЬ!')
    
