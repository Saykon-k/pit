import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки
import matplotlib.pyplot as plt

image = Image.open("files/roof.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
#list_of_grey_value = [];
inc = 0
inc2 = 0
for x in range(width ):
        for y in range(0,-height,-1):
               if (x-720)^2+(y+540)^2 <= 450*1.7:
                   #print(x,y)
                   draw.point((x,-y),(249,166,2) )

image.save("lab_1/cirle_roof.jpg")
del draw
