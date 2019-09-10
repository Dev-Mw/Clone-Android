from django.db import models

class Clone_model(models.Model):
	serial_ip 			= models.CharField(max_length=100)
	ip					= models.CharField(max_length=100, null=True)
	type_status			= models.CharField(max_length=100)
	model 				= models.CharField(max_length=100)
	product				= models.CharField(max_length=100)
	usb					= models.CharField(max_length=100)
	
	class Meta:
		db_table 	= 	'devices'
		managed		=	True

	@classmethod
	def Save_devices(cls, devices):
		devices_db = cls.objects.all()
		if len(devices_db) > 0:
			for x in devices:
				devices = cls.objects.get(serial_ip=x['serial'])
				if x['serial'] != devices.serial_ip:
					new_device = cls(serial_ip=x['serial'], ip=x['ip'], type_status=x['type'], model=x['model'], product=x['product'], usb=x['usb'])
					new_device.save()
		else:
			for x in devices:
				new_device = cls(serial_ip=x['serial'], ip=x['ip'], type_status=x['type'], model=x['model'], product=x['product'], usb=x['usb'])
				new_device.save()

		devices = cls.objects.all()
		return devices

	@classmethod
	def Delete_devices(cls):
		devices = cls.objects.all()
		devices.delete()
		return devices

	@classmethod
	def Get_device(cls, id):
		try:
			device = cls.objects.get(pk=id)
			return device
		except Exception as e:
			return ''
		
		

