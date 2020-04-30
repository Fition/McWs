import asyncio
from send_message import *

def cmd(message,client):
	asyncio.create_task(_cmd(message,client))

async def _cmd(message,client):
	all_ = "agent "
	try:
		for each in message[1:]:
			all_ += each
			all_ += " "
	except:
		await client.send(command("say 傻逼，啥都没有你发个锤子"))
	print(all_)
	await client.send(command(all_))
