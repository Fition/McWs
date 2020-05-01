import time
import asyncio


a = [False,False]

async def printf(a):
	print("Printf a[0] is",a[0])
	if a[0]:
		print("Yes")

async def _main(a):
	while True:
		if a[1]:
			time.sleep(1)
			print("pd")
			await printf(a)
			await asyncio.sleep(0)

async def main(a):
	print("ok")
	asyncio.create_task(_main(a))
	print("ok")
	a[1] = True
	await asyncio.sleep(3)
	a[0] = True
	print("out a[0] is",a[0])

asyncio.get_event_loop().run_until_complete(main(a))
asyncio.get_event_loop().run_forever()
