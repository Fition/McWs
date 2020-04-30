import os
import time
from threading import Thread
import sys

pid = sys.argv[1]
time.sleep(1)
def main():
	os.system("python main.py")
Thread(target=main).start()

os.system("taskkill /f /pid "+str(pid))
pid = os.getpid()
os.system("taskkill /f /pid "+str(pid))
"""
		(OwO)
"""
