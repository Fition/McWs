import asyncio
from image import blocks as bl
import function
from send_message import *

def getblock(pixel):
	try:
		return bl.main[pixel]
	except:
		return "concrete 0"

def onemode(cmd,to_path,arr):
	asyncio.create_task(_onemode(cmd,to_path,arr))

async def _onemode(p,to_path,arr):
	line = arr[0]
	col = arr[1]
	with open(to_path,"a") as f:
		block = getblock(p)
		f.write(f"setblock ~{line} ~ ~{col} {block}\n")
