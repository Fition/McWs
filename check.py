import asyncio
import json

# name 是操作员名字
def getMessageInfo(string,name,bad_packages) -> dict:
	pkt = json.loads(string)
	if "已请求" in string:
		with open("log","a",encoding = "utf-8") as f:
			f.write(str(pkt)+"\n")

		bad_id = int(pkt["header"]["requestId"].split("-")[-1])
		bad_packages.append(bad_id)

	pkt_type = pkt["header"]["messagePurpose"]
	
	# 订阅的回包
	if pkt_type == "event":
		# 具体事件
		pkt_event_type = pkt["body"]["eventName"]
		# 玩家信息
		if pkt_event_type == "PlayerMessage":
			# 发信息的人
			msg_owner = pkt["body"]["properties"]["Sender"]
			msg = pkt["body"]["properties"]["Message"]
			if not "％" in str(pkt):
				print(f"收到一条信息\n发信人:{msg_owner}\n信息内容:{msg}\n")

			# 不是本人操作
			if not msg_owner == name:
				return {"type":"unknown"}
			return {"type":"message","name":msg_owner,"message":msg}

	# 指令回包
	elif pkt_type == "commandResponse":
		return {"type":"command","payload":pkt}

	# 不知道什么东西
	else:
		return {"type":"unknown"}
