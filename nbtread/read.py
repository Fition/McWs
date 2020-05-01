import python_nbt.nbt as nbt
from nbtread.namespace import *
from nbtread import keep
from send_message import *
import function
import json

import asyncio

async def _nbtfile(client,pkt,wait_sympol):
	try:
		# 		nbtfile = read_nbt(pkt[1])
		open(pkt[1],"a").close()
		await client.send(command(status("正在读取,请稍等...")))
		proto = read_nbt(pkt[1])
		await client.send(command(status("已经读取完毕,正在解析数据...")))
		await asyncio.sleep(2)
	except:
		await client.send(command(ok("未找到目标文件")))
		exit()
	"""
	await client.send(command(status("正在读取...")))
	try:
		proto = json.loads(str(nbtfile).replace(" ","").replace("\'","\""))
	except:
		with open("D:\\error","w") as f:
			f.write(str(nbtfile).replace("\'","\""))
	"""
	blocks = proto["blocks"]

	# 方块解析
	file_name = "D:\\TEMP"
	open(file_name,"w").close()
	for each in blocks:
		block_id = each["state"].value
		block_name = proto["palette"][block_id]["Name"].value
		if not block_name == "minecraft:air":
			block_pos = {}
			block_pos["x"] = each["pos"][0].value
			block_pos["y"] = each["pos"][1].value
			block_pos["z"] = each["pos"][2].value
			keep.main(block_pos,block_name,file_name)
# 			await asyncio.sleep(0)
	wait_sympol[0] = True
# 	await client.send(command("testfor @s"))
	await client.send(command(ok("已完成NBT文件解析,开始导入...")))
	await asyncio.sleep(2)
	function.build(["#func","D:\\TEMP",pkt[2]],client)
	await asyncio.sleep(3)
	wait_sympol[0] = False
	"""
	await asyncio.sleep(1)
	wait_sympol[1] = True
	"""

def nbtfile(client,pkt,wait_sympol):
	asyncio.create_task(_nbtfile(client,pkt,wait_sympol))
