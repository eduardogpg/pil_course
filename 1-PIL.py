from PIL import Image #pip install Pillow
#The most important class in the Python Imaging Library is the Image class

try:
	im = Image.open('images/empire.jpg')
	print im.format
	
	im.show()
	im.save("images/news/empire.jpg")

except IOError:
	print ("Imagen no encontrada en la ruta solicitada")
