from PIL import Image, ImageDraw

image = Image.open("/4 semestr/comp_grafic/Lab_1_Jordan_Method _1.1/files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
for x in range(80, width, 160):
    for y in range(height):
        for x1 in range(x,x+80):
            draw.point((x1,y),(0,255,128))
image.show()
#image.save("first.jpg")
del draw
