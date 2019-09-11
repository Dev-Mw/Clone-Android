from subprocess import Popen, PIPE
from random import randrange as rd
from Banners import Banner
import os, sys
import setuptools
import base64


class CloneAndroid(object):

	def __init__(self, port, user, password):
		self.port = port
		self.user = user
		self.password = password

	def __run__(self):
		try:
			self.port = int(self.port)
			return True
		except Exception as e:
			return None


if __name__ == '__main__':
	os.system('clear')

	u = str(rd(10000000)).replace('1','dm').replace('4','kj')
	p = str(rd(10000000)).replace('1','dm').replace('4','qy')

	CA = CloneAndroid(8000, u, p)

	try:
		CA = CloneAndroid(sys.argv[1], u, p)
	except Exception as e:
		pass

	if CA.__run__():
		os.system("echo '{u}|{p}' > c".format(u=CA.user, p=CA.password))
		print(Banner.Banner(CA.port, CA.user, CA.password))
		process = Popen(['python', 'manage.py', 'runserver', '{port}'.format(port=CA.port)], stdout=PIPE, stderr=PIPE)
		(result, error) = process.communicate()
	else:
		print(Banner.BannerInvalid())



		
