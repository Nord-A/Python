from PIL import Image

im  = Image.open('Photo.png')

image = im.load()

print(im.size[0], im.size[1])

print(image[40,40])

#image[250,250] = (0,0,255) Dette er midtpunktet på billedet

image[240,240]

print(image[250, 250]) #refers to pixel index


#Goal is to make a 10x10 square in the middle.
squaresize = 450
temp = int(squaresize / 2)
startpoint = 250 - temp
for x in range(startpoint, startpoint + squaresize):
    for y in range(startpoint, startpoint + squaresize):
        image[x, y] = (255, 0, 0)

im.show()