from PIL import Image

im = Image.open('images/empire.jpg')
print im.mode #The mode of an image defines the type and depth of a pixel in the image.
print im.getpixel((10, 10))

png = Image.open('images/parrot.png')
print png.mode
print png.getpixel( (205, 10) ) #255-255-255
#he Alpha values indicate the transparency or the background factor in the image.

#http://pillow.readthedocs.io/en/3.3.x/handbook/concepts.html#modes
negative = im.convert("L")
print negative.mode
print negative.getpixel( (205, 10) ) #255-255-255
