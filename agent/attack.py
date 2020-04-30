import asyncio
from send_message import *


def attack(message,client):
	asyncio.create_task(_attack(message,client))

async def _attack(message,client):

	# attack_times 默认为 1
	try:
		attack_times = message[1]
	except IndexError:
		attack_times = "1"
	
	# attack_fangxiang 默认为forward
	try:
		attack_fangxiang = message[2]
	except IndexError:
		attack_fangxiang = "forward"

	try:
		# 输入可能不是数字
		time = int(attack_times)
	except:
		await client.send(command(alert("傻逼,让你输入数字你TM给我输入字符串")))
		return

	for i in range(int(attack_times)):
		await client.send(command(f"agent attack {attack_fangxiang}"))
		await asyncio.sleep(0.05)
