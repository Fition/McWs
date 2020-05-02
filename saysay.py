import asyncio
from send_message import *

async def _main(client):
	while True:
		temp = input("说:")
		if temp == "QUIT":
			await client.send(ok("已退出无障碍模式！"))
			return
		print("send")
		await client.send(command(say(temp)))
		print("send2")
		await asyncio.sleep(1)

def main(client):
	asyncio.create_task(_main(client))
