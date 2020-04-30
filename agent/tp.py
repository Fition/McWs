from send_message import *
import asyncio

def tp(message,client):
	asyncio.create_task(_tp(message,client))

async def _tp(message,client):
	try:
		place = message[1:]
	except:
		# 仅仅一个 tp
		place = ["~","~","~"]

	all_ = "agent tp "
	# 拼接
	for each in place:
		all_ += each
	await client.send(command(all_))
