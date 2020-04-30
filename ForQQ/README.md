# Qmirror
*QQMessage in MinecraftBE*
## 这是什么
**在MC中收(发?)QQ消息**
## 如何使用
编辑 main.py 内设置区
``` python
qq = 123456789
authKey = 'WDNMD1145141919'
console_host = '114.514.1919.810:2233'
MineacrftBE_Websocket_port = 9999
```
配置并启动 mirai-console（建议稳定挂服务器）
``` bash
java -jar mirai-console-wrapper-0.3.0.jar
```
安装 python 依赖库并运行
``` python
pip3 install websockets
pip3 install requests
python3 mian.py
```
 - [mirai](https://github.com/mamoe/mirai)
 -  [mirai-console](https://github.com/mamoe/mirai-console/releases)

 -  [http-api](https://github.com/mamoe/mirai-api-http/releases)
