import asyncio
import re
import time

import cmdarg
from send_message import *


async def sendBuildingPackages(client,lines,fps,bad_packages):
	fps = float(fps)
	begin_time = time.time()
	oldjindu = 0
	clock = 0
	await client.send(command("title @a actionbar 进度: 0％"))
	for i in range(len(lines)):
		await client.send(command(lines[i],i))
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

	if len(bad_packages) > 0:
		await asyncio.sleep(3)
	await client.send(command((ok("导入完毕!"))))
	await client.send(command(say(f"本次共导入 {all_blocks_number} 个方块,共用时 {all_time} 秒,平均速度为 {speed} 方块/秒")))
	
	if len(bad_packages) > 0:
		await client.send(command((status("正在进行补包..."))))
		print(bad_packages)
		print("以上为需要补包的指令索引")
		for bad in bad_packages:
			await client.send(command(lines[bad]))
			await asyncio.sleep(0.04)
		bad_packages = []
		# 清理垃圾
		lines = None
		await client.send(command((ok("补包完毕"))))
	await client.send(command((ok("已完成导入"))))

async def getPosAndLines(client,wait_sympol,lines,args):
	await asyncio.sleep(1)
	wait_sympol[0] = True
	await asyncio.sleep(1)
	await client.send(command("testfor @s"))
	await asyncio.sleep(1)

	file_name = args["file_name"]
	fps = args["fps"]

	try:
		fps = float(fps)
	except:
		await client.send(command(alert("错误的值:"+fps)))
		await client.recv()
		await client.recv()
		return

	# 获取玩家坐标
	await client.send(command("tp @s ~~~"))
	result = json.loads(await client.recv())
	try:
		player_pos = result["body"]["destination"]
	except:
		if "外部" in str(result) or "发现" in str(result):
			while True:
				result = json.loads(await client.recv())
				if "外部" in str(result) or "发现" in str(result):
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
	
	wait_sympol[0] = False
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
	return lines

def getArgs(message):
	cmdArgs = cmdarg.Cmd(message)
	args = {}
	try:
		file_name = cmdArgs.get_value("-p")
		args["file_name"] = file_name
	except:
		pass

	try:
		fps = cmdArgs.get_value("-t",40)
		args["fps"] = fps
	except:
		pass

	try:
		size = cmdArgs.get_value("-s",1)
		args["size"] = size
	except:
		pass

	return args
