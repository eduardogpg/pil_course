from PIL import Image, ImageOps

im = Image.open('images/empire.jpg')
mask = Image.open('images/logo.png').convert('RGBA')

output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save('images/news/output.png')
output.show()