from subprocess import Popen, PIPE
import threading
import os
import sys


class Actions(object):

	"""def __init__(self, arg):
		self.arg = arg"""

	def ActiveWlan(self):
		os.system("./exec tcpip 5555")

	def CloneDevice(self, serial_ip, product, model):
		os.system("./exec -s {serial_ip} pull storage ../DEVICES/Product-{product}_Model-{model}/".format(serial_ip=serial_ip, product=product, model=model))
		return "ok"

	def GetDevices(self):
		process 		= Popen(["./exec","devices","-l"], stdout=PIPE, stderr=PIPE)
		(result, error) = process.communicate()
		return result

	def Ips(self, ip):
		proces 				= Popen(["./exec", "-s", "{ip}".format(ip=ip), "shell", "ip", "-oneline", "-f", "inet", "addr", "show", "wlan0"], stdout=PIPE, stderr=PIPE)
		(result, error) 	= proces.communicate()
		devicesIP 			= result.decode().split(" ")
		try:
			return devicesIP[6]
		except Exception as e:
			return ''

	def ConnectDevice(self, ip):
		os.system("./exec connect {ip}:5555".format(ip=ip))
		process = Popen(["./exec", "connect", "{ip}:5555".format(ip=ip)], stdout=PIPE, stderr=PIPE)
		(result, error) = process.communicate()
		return result

	def ReconnectDevice(self, ip):
		os.system("./exec -s {ip}:5555 reconnect".format(ip=ip))
		return ''

Actions = Actions()

