import asyncio

async def main(client,command):
	while True:
		cmd = input("请指示: ")
		if cmd == "exit":
			await client.send(command("say 服务端"))
		await client.send(command(cmd))
		while await client.recv():
			pass
