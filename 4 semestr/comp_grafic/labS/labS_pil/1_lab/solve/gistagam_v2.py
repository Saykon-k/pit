from PIL import Image, ImageDraw

image = Image.open("../files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
green = 256*[0]
red = 256*[0]
blue = 256*[0]
grey = 256*[0]

for x in range(width):
    for y in range(height):
        a = pix[x, y][0]
        b = pix[x, y][1]
        c = pix[x, y][2]
        green[b]+=1
        red[a]+=1
        blue[c]+=1
        grey[int((a+b+c)/3)]+=1

gr = height/(max(green)*2)
re = height/(max(red)*2)
bl = height/(max(blue)*2)
gre = height/(max(grey)*2)

print(max(green),' ',gr,' ',height,' ',max(green)*gr)
for i in range(256):
    green[i]=round(gr*green[i])
    blue[i]=round(bl*blue[i])
    red[i] = round(re*red[i])
    grey[i] = round(gre*grey[i])

for x in range(256):
    for y in range(height):
        if y > height/2-green[x]:
            if y < height/2:
                draw.point((x,y),(0,255,0))

for x in range(256 , 512):
    for y in range(height):
        if y > height / 2 - red[x-256]:
            if y < height / 2:
                draw.point((x, y), (255, 0, 0))

for x in range(512 , 768):
    for y in range(height):
        if y > height / 2 - blue[x-512]:
            if y < height / 2:
                draw.point((x, y), (0, 0, 255))
for x in range(768 , 1024):
    for y in range(height):
        if y > height / 2 - grey[x-768]:
            if y < height / 2:
                draw.point((x, y), (128, 128, 128))



image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//gistagram_all.jpg")
del draw
