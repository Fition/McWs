import asyncio
import json
import time
import traceback
import re

from send_message import *
import cmdarg
import api


def build(message,client,wait_sympol,bad_packages):
	asyncio.create_task(_build(message,client,wait_sympol,bad_packages))

async def _build(message,client,wait_sympol,bad_packages):
	args = api.getArgs(message)
	try:
		open(args["file_name"],"r").close()
	except:
		await client.send(command(alert("您的文件路径输入有误,无法找到您的文件!")))
		await client.recv()
		await client.recv()
		return

	with open(args["file_name"],"r") as f:
		lines = f.readlines()
	lines = await api.getPosAndLines(client,wait_sympol,lines,args)
	await api.sendBuildingPackages(client,lines,args["fps"],bad_packages)
