import websockets as ws
import asyncio
import json
import random
import time
import os
import socket

import packages
import init
import send_message as _sm
import check


os.system("cls")
wait_sympol = [False,]

def getPlayerInfo(string) -> str:
	pkt = json.loads(string)
	try:
		name = pkt["body"]["victim"][0]
	except:
		pid = os.getpid()
		os.system("taskkill /pid /f "+str(pid))
	return name

async def is_wait(pkt,wait_sympol):
	# 导入建筑时，需要确定玩家坐标，需要接收指令回包，这时就必须保证指令回包不被主进程抢走
	try:
		if "#func" in pkt["message"]:
			await asyncio.sleep(2)
	except:
		pass
	try:
		if wait_sympol[0]:
			while wait_sympol[0]:
				await asyncio.sleep(0.1)
	except:
		pass

async def main(client,*args):
	await client.send(_sm.command("testfor @s"))
	name = getPlayerInfo(await client.recv())

	await client.send(_sm.command(_sm.actionbar("§b<<< 欢迎使用 >>>")))
	await client.send(_sm.command(_sm.status("正在接收订阅数据包...")))
	await asyncio.sleep(2)
	await client.send(json.dumps(packages.main["subscribe"]))
	await client.send(_sm.command(_sm.ok("已经接收订阅数据包!")))
	await client.send(_sm.command(_sm.say("作者:阖庐(GhostWorker)")))
	await client.send(_sm.command(_sm.say("操作员: "+name)))
	
	# 用于收集指令回包
	commandResults = []
	# 用于补包
	bad_packages = []
	while True:
		pkt = check.getMessageInfo(await client.recv(),name,bad_packages)
		asyncio.create_task(
				init.main(pkt,client,_sm.command,commandResults,		# normal
					wait_sympol,			# 阻塞主线程用
					bad_packages			# 补包用
					)
				)
		# 判断是否需要阻塞
		await is_wait(pkt,wait_sympol)
		await asyncio.sleep(0)

server = ws.serve(main,'',1234)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
