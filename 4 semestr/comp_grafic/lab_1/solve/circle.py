from PIL import Image, ImageDraw

image = Image.open("../files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

for x in range(1, width, 80):
    for y in range(360, 720 ,1):
        for x1 in range(x,x+40):
            draw.point((x1,y),(0,255,0))

for x in range(width ):
        for y in range(height):
               if (x-720)**2+(y-540)**2 <= 300**2:
                   draw.point((x,y),(249,166,2) )

image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//cirle_roof.jpg")
del draw
