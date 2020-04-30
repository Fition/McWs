from PIL import Image

img = Image.open("test.jpg").convert("P")

print(img.getpixel((10,10)))
