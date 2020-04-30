import asyncio
from send_message import *

def main(pkt,client):
	asyncio.create_task(_main(pkt,client))

async def _main(pkt,client):
	msg = pkt["message"]
	if "Hello" in msg or "Hi" in msg or "hello" in msg:
		await client.send(command("say 干啥"))

	elif "?" in msg or "？" in msg:
		await client.send(command("say 问个锤子，啥都不知道，就知道问问问"))
