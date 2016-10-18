from PIL import Image

im = Image.open('images/empire.jpg')
rotate = im.rotate(30, expand = True)
#rotate.show()

"""
to rotate the image in 90 degree steps, you can either use the rotate method or the transpose method
Image.FLIP_LEFT_RIGHT
Image.FLIP_TOP_BOTTOM
Image.ROTATE_90
Image.ROTATE_180
Image.ROTATE_270
"""

transpose =  im.transpose(Image.ROTATE_90)
transpose.show()
transpose.save("images/news/empire.jpg")