import random
i1 = int (input())
i = random.randint(0,10)
if i==i1:
    print('победа')
else:
    print('Попробуйте еще раз!!!')
    if i<i1:
        print('ваше число больше, чем было загаданно...')
    else:
        print('ваше число меньше, чем было загаданно...')
