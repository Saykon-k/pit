from PIL import Image, ImageDraw

image = Image.open("../files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
green = 256*[0]
red = []
blue = []

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        green[b]+=1
        red.append(a)
        blue.append(c)

gr= height/(max(green)*2)
print(max(green),' ',gr,' ',height,' ',max(green)*gr)
for i in range(256):
    green[i]=round(gr*green[i])

for x in range(256):
    for y in range(height):
        if y > height/2-green[x]:
            if y < height/2:
                draw.point((x,y),(0,255,0))




image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//green_kom.jpg")
del draw
