from PIL import Image
from image import put
import asyncio
import function

def pic(message,client):
	# #pic xxx.jpg xxx.mcfunction t:20 1
	file_path = message[1]
	to_path = message[2]
	t_arg = message[3]
	chuyi_can = int(message[4])

	img = Image.open(file_path).convert("P")
	width,height = img.size
	img = img.resize((int(width/chuyi_can),int(height/chuyi_can)))
	width,height = img.size

	open(to_path,"w").close()
	for h in range(height):
		for w in range(width):
			pixel = img.getpixel((w,h))
			put.onemode(pixel,to_path,(w,h))

# 	message = ["#func",to_path,t_arg]
# 	asyncio.create_task(function.build(message,client))
