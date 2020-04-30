import asyncio

class __init__:
	def __init__(self):
		self.text = None

glo = __init__()
glo.text = "fuck"

async def main():
	print(glo.text)

asyncio.get_event_loop().run_until_complete(main())
