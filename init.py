import asyncio
import os

from send_message import *
import please_tell
import agent
import take_water
import function
import image
import re
import ForQQ
import nbtread
import saysay


async def main(pkt,client,command,commandResults,			# normal
		wait_sympol,			# 阻塞主线程用
		bad_packages			# 补包用
		):
	# 判断是否为玩家信息，有可能是指令回包
	if pkt["type"] == "message":
		message = pkt["message"].split(" ")
		# 用于处理连续的多个空格
		removes = []			#咋还没加载ideavimrc？
		for i in range(len(message)):
			message[i] = message[i].replace(" ","")
			if message[i] == "":
				removes.append(i)

		for each in removes:
			message.pop(each)
		# ===============================================================

		if pkt["type"] == "message":
			cmd = message[0]
			
			# 涉及建筑导入部分
			if re.search(r"^#func",cmd):
				function.build(message,client,wait_sympol,bad_packages)

			elif re.search(r"^#nbt",cmd):
				nbtread.nbtfile(client,message,wait_sympol,bad_packages)

			elif re.search("^#pic",cmd):
				image.pic(message,client,wait_sympol,bad_packages)

			# =========== 其他部分 =================================================

			elif re.search(r"^#ag-create",cmd):
				await client.send(command("agent create"))

			elif re.search(r"^#ag-attack",cmd):
				agent.attack(message,client)

			elif re.search(r"^#ag-tp",cmd):
				# 传 pkt 为了传送方便
				agent.tp(message,client)

			elif re.search(r"^#ag-cmd",cmd):
				agent.cmd(message,client)


			elif re.search(r"^#qqmsg",cmd):
				await client.send(command(say("如果您希望更改账号配置，请修改config.py中的相关内容~~~")))
				ForQQ._main(client,commandResults)

			elif re.search(r"^#炸服助手",cmd):
				take_water.main(client,wait_sympol)


			elif re.search(r"^#无障碍模式",cmd):
				saysay.main(client)

			elif re.search("^#shutdown",cmd):
				pid = os.getpid()
				os.system(f"taskkill /f /pid {pid}")
				os.system(f"kill {pid}")

			elif re.search("^#restart",cmd):
				os.system("python restart.py "+str(os.getpid()))

			else:
				take_water.main(pkt,client)
