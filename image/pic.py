from PIL import Image
from image import blocks as bl
from send_message import *
import asyncio
import traceback
import function
import cmdarg
import api

def pic(message,client,wait_sympol,bad_packages):
	asyncio.create_task(_pic(message,client,wait_sympol,bad_packages))

async def _pic(message,client,wait_sympol,bad_packages):
	args = api.getArgs(message)
	file_name = args["file_name"]
	size = args["size"]
	fps = args["fps"]

	try:
		size = float(size)
	except:
		await client.send(command(alert("错误的参数:"+str(size))))
		return
	
	try:
		img = Image.open(file_name).convert("P")
		await client.send(command(status("正在识别图片...")))
	except:
		await client.send(command(alert("未找到文件！")))
		return
	width,height = img.size
	img = img.resize((int(width/size),int(height/size)))
	width,height = img.size
	
	lines = []
	for h in range(height):
		for w in range(width):
			pixel = img.getpixel((w,h))
			try:
				block = bl.main[pixel]
			except:
				block = "concrete 0"
			lines.append(f"setblock ~{w} ~ ~{h} {block}")
	
	await client.send(command(ok("识别完毕！")))

	await api.getPosAndLines(client,wait_sympol,lines,args)
	await api.sendBuildingPackages(client,lines,fps,bad_packages)
