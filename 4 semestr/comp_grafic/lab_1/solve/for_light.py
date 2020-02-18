from PIL import Image, ImageDraw

image = Image.open("../files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()
inc = 0
inc2 = 0
for x in range(width-1, 1 , -1):
        for y in range(height-1,1,-1):
                a = pix[x, y][0]
                b = pix[x, y][1]
                c = pix[x, y][2]

                draw.point((x,y),(a-inc,b-inc,c-inc))
        inc2+=1
        if inc2 == 6:
                inc += 1
                inc2 = 0
image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//light_roof.jpg")
del draw
