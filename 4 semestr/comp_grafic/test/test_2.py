from PIL import Image, ImageDraw

image = Image.open("../lab_1/files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
for x in range(width ):
        for y in range(height):
               if (x)**2+(y-540)**2 <= 540**2:
                   a = pix[x, y][0]
                   b = pix[x, y][1]
                   c = pix[x, y][2]
                   draw.point((x,y),(255-a,255-b, 255-c))
image.show()
image.save("second.jpg")
del draw
