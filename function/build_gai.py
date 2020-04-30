import asyncio
import json
import time
import re
from send_message import *

def build(message,client):
	asyncio.create_task(_build(message,client))

async def _build(message,client):
	try:
		file_name = message[1]
	except IndexError:
		file_name = "G:\\python\\projects\\minecraft\\function\\files\\fun1.mcfunction"
	
	fps = "50"
	try:
		for each in message[2:]:
			each = each.split(":")
			if each[0] == "":
				pass
			elif each[0] == "t":
				fps = each[1]
			else:
				await client.send(command(alert("错误的参数:"+each[0])))
				await client.recv()
				await client.recv()
	except IndexError:
		fps = "50"
	
	try:
		fps = float(fps)
	except:
		await client.send(command(alert("错误的值:"+fps)))
		await client.recv()
		await client.recv()
		return
	
	try:
		open(file_name,"r").close()
	except:
		await client.send(command(alert("您的文件路径输入有误,无法找到您的文件!")))
		await client.recv()
		await client.recv()
		return

	with open(file_name,"r") as f:
		lines = f.readlines()
		
		# 获取玩家坐标
		await client.send(command("tp @s ~~~"))
		result = json.loads(await client.recv())
		try:
			player_pos = result["body"]["destination"]
		except:
			await client.send(command(alert("请稍等一会，您的世界处理不了这么多方块~~~")))
			return
		for each in player_pos:
			player_pos[each] = int(player_pos[each])
		
		await client.send(command(status("正在将相对坐标转换为绝对坐标...")))
		for i in range(len(lines)):
			time = 0		# 用来计算坐标是 x , y 还是 z
			cmd = lines[i].split(" ")
			# cmd = [setblock,~-8,~-32,~-4,stained_hardened_clay,10]
			for each in cmd:
				# each = "~-8"
				if "~" in each:
					# pos = ["-8"]
					pos = each.split("~")
					pos.pop(0)
					for j in pos:
						# i = -8
						try:
							j = int(j)
						except:
							j = 0
						# x 轴
						if time == 0 or time == 3:
							j = player_pos["x"] + j
							pos
						if time == 1 or time == 4:
							j = player_pos["y"] + j
						if time == 2 or time == 5:
							j = player_pos["z"] + j
						
						cmd_span = re.search(r"~-*\d*",lines[i]).span()
						cmd_pos = lines[i][cmd_span[0]:cmd_span[1]]
						lines[i] = lines[i].replace(cmd_pos,str(j)+" ",1)
						time += 1
		await client.send(command(status("转换完毕! 正在导入建筑... 期间您可以自由活动")))
		
		while True:
			recvs = []
			most = False			# 指令未被拒绝
			for each in lines:
				await client.send(command(each))
				print(await client.recv())
				"""
				recvs.append(await client.recv(),each)
	# 			await asyncio.sleep(fps/1000)
			# 检查是否有遗漏
			for each in recvs:
				if "请求" in each[0]:
					await client.send(command(each[1]))
					most = True
			if not most:
				break
			"""
			break

		await client.send(command((ok("导入完毕!"))))
