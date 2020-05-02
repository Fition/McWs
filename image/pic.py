from PIL import Image
from image import put
from send_message import *
import asyncio
import traceback
import function
import cmdarg

def pic(message,client,wait_sympol,bad_packages):
	asyncio.create_task(_pic(message,client,wait_sympol,bad_packages))

async def _pic(message,client,wait_sympol,bad_packages):
	args = cmdarg.Cmd(message)
	file_path = args.get_value("-p")
	chuyi = args.get_value("-s",1)
	fun_fps = args.get_value("-t",40)

	try:
		chuyi = int(chuyi)
	except:
		await client.send(command(alert("错误的参数:"+chuyi)))
		return
	
	try:
		img = Image.open(file_path).convert("P")
		await client.send(command(status("正在识别图片...")))
	except:
		await client.send(command(alert("未找到文件！")))
		return
	width,height = img.size
	img = img.resize((int(width/chuyi),int(height/chuyi)))
	width,height = img.size

	open("TEMP.ghostworker","w").close()
	for h in range(height):
		for w in range(width):
			pixel = img.getpixel((w,h))
			put.onemode(pixel,"TEMP.ghostworker",(w,h))
	
	await client.send(command(ok("识别完毕！")))

	message = ["#func","-p","TEMP.ghostworker","-t",str(fun_fps)]
	asyncio.create_task(function.build(message,client,wait_sympol,bad_packages))
