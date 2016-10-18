from PIL import Image

im = Image.open('images/empire.jpg')
print im.size
print im.width
print im.height

im = im.resize((im.width / 2, im.height / 2))
im = im.rotate(120)
im.show()