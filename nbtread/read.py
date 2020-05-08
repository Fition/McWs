import asyncio
import os
import python_nbt.nbt as nbt
import json

from send_message import *
from nbtread import keep
from nbtread.namespace import *
from nbtread import datavalue
import function
import cmdarg
import api


async def _nbtfile(client,message,wait_sympol,bad_packages):
	try:
		args = cmdarg.Cmd(message)
		file_path = args.get_value("-p")
		fun_fps = args.get_value("-t")

		open(file_path,"a").close()
		file_size = os.path.getsize(file_path)
		if file_size < 1024*512:
			say_size = int(file_size/1024)
			danwei = "KB"
		else:
			say_size = file_size/1024/1024
			danwei = "MB"

		# 速度 1：		8KB		
		pay_time = file_size/1
		await client.send(command(say(f"文件大小为: {say_size}{danwei}")))
		await client.send(command(status("正在读取,请稍等...")))

		read_time = int(file_size/(2.8*1024))		# 经测算，建筑大小与读取所用时间数值之比大约为 2.8:1
		await client.send(command(say(f"预计读取和解析时间共需 {read_time} 秒")))
		await asyncio.sleep(0)
		proto = read_nbt(file_path)
		await client.send(command(status("已经读取完毕,正在解析数据...")))
		await asyncio.sleep(1)
	except:
		await client.send(command(alert("未找到目标文件")))
		return

	blocks = proto["blocks"]

	# 方块解析
	lines = []
	for each in blocks:
		block_id = each["state"].value
		block_name = proto["palette"][block_id]["Name"].value
		if not block_name == "minecraft:air":
			block_name = datavalue.getBlockValue(block_name,block_id,proto)
			block_pos = {}
			block_pos["x"] = each["pos"][0].value
			block_pos["y"] = each["pos"][1].value
			block_pos["z"] = each["pos"][2].value

			localpos = ""
			for each in block_pos:
				if block_pos[each] == 0:
					localpos += "~"
				else:
					localpos += "~" + str(block_pos[each])
			block_name = block_name.replace("minecraft:","")
			lines.append(f"setblock {localpos} {block_name}")

	await client.send(command(ok("已完成NBT文件解析,开始导入...")))
	
	args = api.getArgs(message)

	await api.getPosAndLines(client,wait_sympol,lines,args)
	await api.sendBuildingPackages(client,lines,args["fps"],bad_packages)

def nbtfile(client,message,wait_sympol,bad_packages):
	asyncio.create_task(_nbtfile(client,message,wait_sympol,bad_packages))
