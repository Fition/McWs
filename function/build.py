import asyncio
import json
import time
import traceback
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
	
	if fps < 15.625:
		await client.send(command(alert("延迟最小要设为 15.625 !")))
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
			if "NBT" in str(result):			# NBT 的提示下一个包就是 testfor 回包
				while True:
					result = json.loads(await client.recv())
					if "已完成" in str(result):
						pass
					else:
						break
				try:
					player_pos = result["body"]["destination"]
				except:
					print("="*80)
					print(result)
					print("="*80)
					await client.send(command(alert("请稍等一会，您的世界处理不了这么多请求~~~")))
					return
			else:
				print("-"*20)
				print(result)
				print("-"*20)
				return
		for each in player_pos:
			player_pos[each] = int(player_pos[each])
		
		await client.send(command(status("正在将相对坐标转换为绝对坐标...")))
		for i in range(len(lines)):
			time_ = 0		# 用来计算坐标是 x , y 还是 z
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
						if time_ == 0 or time_ == 3:
							j = player_pos["x"] + j
						if time_ == 1 or time_ == 4:
							j = player_pos["y"] + j
						if time_ == 2 or time_ == 5:
							j = player_pos["z"] + j
						
						cmd_span = re.search(r"~-*\d*",lines[i]).span()
						cmd_pos = lines[i][cmd_span[0]:cmd_span[1]]
						lines[i] = lines[i].replace(cmd_pos,str(j)+" ",1)
						time_ += 1
		await client.send(command(status("转换完毕! 正在导入建筑... 期间您可以自由活动")))
		
		begin_time = time.time()
		oldjindu = 0
		clock = 0
		await client.send(command("title @a actionbar 进度: 0％"))
		for i in range(len(lines)):
			await client.send(command(lines[i]))
			jindu = int(i/len(lines)*100)
			if jindu > oldjindu:
				await client.send(command(f"title @a actionbar 进度: {jindu}％"))
				oldjindu = jindu
			if not clock % 4:
				await asyncio.sleep(fps/1000)
			clock += 1
		
		await client.send(command("title @a actionbar 进度: 100％"))

		end_time = time.time()
		# 统计信息
		all_time = int(end_time - begin_time)
		all_blocks_number = len(lines)
		speed = int(all_blocks_number / all_time)
		# 清理垃圾
		lines = None

		await client.send(command((ok("导入完毕!"))))
		await client.send(command(say(f"本次共导入 {all_blocks_number} 个方块,共用时 {all_time} 秒,平均速度为 {speed} 方块/秒")))
