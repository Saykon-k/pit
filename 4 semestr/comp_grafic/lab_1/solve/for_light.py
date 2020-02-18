import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки
import matplotlib.pyplot as plt

image = Image.open("../files/roof.JPG") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
#list_of_grey_value = [];
inc = 0
inc2 = 0
for x in range(width-1, 1 , -1):
        for y in range(height-1,1,-1):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]

                draw.point((x,y),(a-inc,b-inc,c-inc))
        inc2+=1
        if inc2 == 6:
                inc += 1
                inc2 = 0
image.save("lab_1/light_roof.jpg")
del draw
