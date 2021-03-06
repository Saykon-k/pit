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
for x in range(width):
        for y in range(height):
                if y < height / 2:
                        draw.point((x, y), (64, 64, 64))

                #draw.point((x, y), (x, x, x))

                #yellow_bear
                # if a < 200 and  b < 200 and c < 200 :
                #         draw.point((x, y), (a, b, c))
                # else:
                #         draw.point((x,y), (253,233,16))

                #yellow
                #draw.point((x,y),(255,255,0))

                #negative_roof
                #draw.point((x,y),(255-a,255-b,255-c))

                #shades_of_gray_roof
                # avarage_value = int ((a+b+c)/3)
                # draw.point((x,y),(avarage_value,avarage_value,avarage_value))

                #sepia_roof
                # avarage_value = int((a + b + c) / 3)
                # draw.point((x,y), (avarage_value+25*2,avarage_value+25,avarage_value))

                #white_and_black_roof
                # if a > 80 and b > 80 and c > 80 :
                #         draw.point((x,y),(255,255,255))
                # else:
                #         draw.point((x,y),(0,0,0))

                #tone_del_2
                #draw.point((x,y),(int(a/2),int(b/2),int(c/2)))

                # 3_color_roof
                # более правильное решение - написать три цикла, чтобы не было постоянной проверки, но это же питон здесь все равно будет медленно
                # avarage_value = int((a + b + c) / 3)
                # if x < width/3:
                #         draw.point((x,y),(avarage_value,avarage_value,0))
                # elif x < width*2/3:
                #         draw.point((x,y),(avarage_value,0,0))
                # else:
                #         draw.point((x,y),(0,avarage_value,0))

                #green_komp_for lake
                #list_of_green_value.append(b);

                #red_komp_for lake
                #list_of_red_value.append(a)

                # #blue_komp_for_kale
                # list_of_blue_value.append(c)

                #grey_komp_for_lake
                # avarage_value = int((a + b + c) / 3)
                # list_of_grey_value.append(avarage_value)

                #iantarny_roof NAN


# plt.hist(list_of_green_value, 255)
# plt.savefig("F:/pit/4 semestr/comp_grafic/lab_1/out/green_komp_for_lake.png")

# plt.hist(list_of_red_value, 255)
# plt.savefig("F:/pit/4 semestr/comp_grafic/lab_1/out/red_komp_for_lake.png")

# plt.hist(list_of_blue_value, 255)
# plt.savefig("F:/pit/4 semestr/comp_grafic/lab_1/out/blue_komp_for_lake.png")

# plt.hist(F:/pit/4 semestr/comp_grafic/lab_1/out/list_of_grey_value, 255)
# plt.savefig("F:/pit/4 semestr/comp_grafic/lab_1/out/grey_komp_for_lake.png")
image.show()
image.save("F:/pit/4 semestr/comp_grafic/lab_1/out/Nan1.jpg")
del draw
