import random
from PIL import Image, ImageDraw
def corect(r,r_a,r_b):
    return(r - r_a) * 255 // (r_b - r_a)
def min_a(gist):
    i = 0
    while gist[i] <= min:
        i+=1
    return i
def min_b(gist):
    i = 255
    while gist[i] <= min:
        i-=1
    return i

image = Image.open("../files/lego.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

gistRed = [0]*256
gistGreen = [0]*256
gistBlue = [0]*256
gistBrightness = [0]*256

for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            gistRed[r] += 1
            gistGreen[g] += 1
            gistBlue[b] += 1
min = 230

r_a = min_a(gistRed)
r_b = min_b(gistRed)

g_a = min_a(gistGreen)
g_b = min_b(gistGreen)

b_a = min_a(gistBlue)
b_b = min_b(gistBlue)

for x in range(width-1):
    for y in range(height):
        r = pix[x, y][0]
        g = pix[x, y][1]
        b = pix[x, y][2]
        draw.point((x,y),(corect(r,r_a,r_b),corect(g,g_a,g_b),corect(b,b_a,b_b)))
image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//lego.jpg")
