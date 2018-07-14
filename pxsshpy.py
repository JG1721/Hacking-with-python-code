#!/usr/bin/python

from pexpect import pxssh
import sys


def connect(addr,username,password):
	user=username
	passwd=password
	print("Trying to connect...")

	try:
		s= pxssh.pxssh()
		if not (s.login(addr,user,passwd)):
			print("SSH Connection failed")
		else:
			print("SSH connection established with "+user+" : "+passwd)
			s.sendline('whoami')
			s.prompt()
			print(s.before)
			s.logout()
			
	except Exception as r:
		print(r)

if len(sys.argv) < 4:
	print('Not enough arguments\n>>hostname,username,password required.')
else:
	address=sys.argv[1]
	username=sys.argv[2]
	password=sys.argv[3]
	connect(address,username,password)	

