import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки
import matplotlib.pyplot as plt

image = Image.open("../files/roof.JPG") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
for x in range(1, width, 80):
    for y in range(360, 720 ,1):
        for x1 in range(x,x+40):
            draw.point((x1,y),(0,255,0))
for x in range(width ):
        for y in range(height):
               if (x-720)**2+(y-540)**2 <= 300**2:
                   draw.point((x,y),(249,166,2) )

image.save("lab_1/cirle_roof.jpg")
del draw
