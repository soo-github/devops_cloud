# pip install pillow

from PIL import Image

im = Image.open("static/dog.jpg")
im.thumbnail((800, 600))
im.save("static/dog.jpg")
