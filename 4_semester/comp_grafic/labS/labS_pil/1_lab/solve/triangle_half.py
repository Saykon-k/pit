from PIL import Image, ImageDraw

image = Image.open("../files/roof.JPG")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

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

image.save("F:/pit/4 semestr/comp_grafic/lab_1/out//two_triangle.jpg")
del draw
