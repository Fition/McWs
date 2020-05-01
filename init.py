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

async def main(pkt,client,command,commandResults,wait_sympol):
	# 判断是否为玩家信息，有可能是指令回包
	if pkt["type"] == "message":
		message = pkt["message"].split(" ")
		if pkt["type"] == "message":
			cmd = message[0]

			if re.search(r"^#ag-create",cmd):
				await client.send(command("agent create"))

			elif re.search(r"^#ag-attack",cmd):
				agent.attack(message,client)

			elif re.search(r"^#ag-tp",cmd):
				# 传 pkt 为了传送方便
				agent.tp(message,client)

			elif re.search(r"^#ag-cmd",cmd):
				agent.cmd(message,client)

			elif re.search(r"^#func",cmd):
				function.build(message,client)

			elif re.search("^#pic",cmd):
				image.pic(message,client)

			elif re.search(r"^#qqmsg",cmd):
				await client.send(command(say("如果您希望更改账号配置，请修改config.py中的相关内容~~~")))
				ForQQ._main(client,commandResults)

			elif re.search(r"^#nbt",cmd):
				nbtread.nbtfile(client,message,wait_sympol)

			elif re.search("^#shutdown",cmd):
				pid = os.getpid()
				os.system(f"taskkill /f /pid {pid}")
				os.system(f"kill {pid}")

			elif re.search("^#restart",cmd):
				os.system("python restart.py "+str(os.getpid()))

			else:
				take_water.main(pkt,client)
