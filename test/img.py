from PIL import ImageDraw,Image

image = Image.open("flower.png").convert("P")
newimage = Image.new("P",(100,100),image.getpixel((2,2)))
newimage.save("to.gif")
