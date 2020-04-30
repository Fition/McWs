import websockets
import asyncio
import requests
import json
import socket
import config as cfg

qq = cfg.qq
authKey = cfg.authKey
console_host = cfg.console_host
MineacrftBE_Websocket_port = cfg.MineacrftBE_Websocket_port
enablews = cfg.enablews


def get_host_ip():
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.connect(('8.8.8.8', 80))
    ip = so.getsockname()[0]
    so.close()
    return ip


def qq_init():
    data = '''{"authKey": "%s"}''' % authKey
    res = requests.post("http://%s/auth/" % console_host, data=data)
    session = json.loads(res.text)['session']
    data = '''{"sessionKey": %s,"qq": %s}''' % (session, qq)
    requests.post("http://%s/verify/" % console_host, data=data)
    res = requests.get("http://%s/config?sessionKey=" % console_host + session, data=data)
    print(res.text)
    return session


async def fetch_qq(session):
    async with websockets.connect('ws://%s/message?sessionKey=%s' % (console_host, session)) as qq_websocket:
        recv_text = await qq_websocket.recv()
        print(f"{recv_text}")
        J = json.loads(recv_text)
        if J['type'] == 'FriendMessage':
            G = '私'
            N = J['sender']['nickname']
            Id = J['sender']['id']
        elif J['type'] == 'GroupMessage':
            G = J['sender']['group']['name']
            Id = "群|%d" % J['sender']['group']['id']
            N = J['sender']['memberName']
        MessageChain = J['messageChain']
        M = ''
        for i in MessageChain[1:]:
            if i['type'] == 'Image':
                M += "§7" + i['imageId']
            elif i['type'] == 'Plain':
                M += "§3" + i['text']
            elif i['type'] == 'At':
                M += "§e" + i['display']
            elif i['type'] == 'Face':
                M += "§d" + i['name']
            elif i['type'] == 'AtAll':
                M += "§e全体成员"
        return G, Id, N, str(M).replace('"', '\"')


async def send_to_mc(mc_websocket, msg):
    command = '''{"body": {"origin": {"type": "player"},"commandLine": "say §6<%s>§1(%s)§7[%s]:%s","version": 1},
    "header": {"requestId": "00000000-0000-0000-0000-0000WDNMD000","messagePurpose": "commandRequest","version": 1,
    "messageType": "commandRequest"}} '''
    await mc_websocket.send(command % msg)


async def main(mc_websocket):
    session = qq_init()
    while True:
        msg = await fetch_qq(session)
        await send_to_mc(mc_websocket, msg)

def _main(mc_websocket):
	asyncio.create_task(main(mc_websocket))

if __name__ == '__main__':
    print(f"请在MCBE里输入 /connect {get_host_ip()}:{MineacrftBE_Websocket_port}")
    Minecraft_Websocket_Server = websockets.serve(main, '0.0.0.0', MineacrftBE_Websocket_port)
    asyncio.get_event_loop().run_until_complete(Minecraft_Websocket_Server)
    asyncio.get_event_loop().run_forever()
