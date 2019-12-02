from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
from django.forms.models import model_to_dict
from models.Clone_model import Clone_model
from functions import Actions
import os

def Index(request):
	return render(request, 'index.html', {'pk':''})

def Login(request, user, password):
	file = open("c","r")
	fp = file.read()[:-1]
	fp = fp.split("|")
	file.close()

	if fp[0] == user and fp[1] == password:
		return render(request, 'index.html', {'pk':'ok'})
	else:
		return render(request, 'index.html', {'pk':'','ar':''})

def DevicesOn(request):
	Clone_model.Delete_devices()
	deviceT = Actions.GetDevices()
	devices = []
	print(deviceT)
	for device in deviceT.decode().split("\n")[1:][:-2]:
		deviceC = device.split(" ")
		deviceF = []
		for x in deviceC:
			if x != '':
				deviceF.append(x)
				
		if 'unauthorized' not in deviceF:
			wlan0 = Actions.Ips(deviceF[0])
			if wlan0 != '':
				devices.append({"serial":deviceF[0], "ip":wlan0, "type": deviceF[1], "usb": deviceF[2], "product": deviceF[3], "model": deviceF[4], "device": deviceF[5]})
		else:
			devices.append({"serial":deviceF[0], "ip":"Unauthorized", "type": "Unauthorized", "usb": deviceF[2], "product": "Unauthorized", "model": "Unauthorized", "device": "unauthorized"})
	
	activeWlan = Actions.ActiveWlan()
	devices = Clone_model.Save_devices(devices)
	devices = [model_to_dict(x) for x in devices]
	return JsonResponse({'devices':devices}, status=200)


def CloneDevice(request, id_device):
	device = Clone_model.Get_device(id_device)
	if device == '':
		return JsonResponse({'data':[]}, status=200)
	else:
		clone_device = Actions.CloneDevice(device.serial_ip, device.product, device.model)
		return JsonResponse({'data': clone_device}, status=200)
	

def ConnectDevice(request, ip):
	connection = Actions.ConnectDevice(ip)
	if connection.decode()[:-1] == 'already connected to {ip}:5555'.format(ip=ip):
		Actions.ReconnectDevice(ip)
		return JsonResponse({'data':[]}, status=200)
	else:
		return JsonResponse({'data':'ok'}, status=200)


