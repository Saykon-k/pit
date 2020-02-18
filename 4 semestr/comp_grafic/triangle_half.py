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
for x in range(width):
        for y in range(height):
                # triangle_half
                # if y<= 0.75*x:
                #         draw.point((x,y),(255,255,0))

                #two_triangle
                # if y <= 0.75*x and y >= -0.75*x+1080:
                #         draw.point((x,y),(172,74,245))
                # if y >= 0.75*x and y <= -0.75*x+1080:
                #         draw.point((x,y),(172,74,245))
                print()

print(width)
print(height)

image.save("lab_1/two_triangle.jpg")
del draw
