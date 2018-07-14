#!/usr/bin/python

import paramiko
import socket
import sys

e=0
def param_ssh(addr,user,passwd):
	global e
	username=user
	password=passwd
	address=addr
	
  	print("Connecting to server...")
       	client = paramiko.SSHClient()
       	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		sock=socket.socket()
		ip=socket.gethostbyname(address)
		client.connect(ip, username=username, password=password, look_for_keys=False)
		
	except Exception as r:
		e=1
		print("[-]"+str(r)+" \nWrong credentials "+username+":"+password)
	
		
	if(e==0):
		print("Connected Successfully with "+username+":"+password)
		stdin,stdout,stderr=client.exec_command('whoami')
		outlines=stdout.readlines()
		resp=''.join(outlines)
		print(resp)
		
if len(sys.argv) < 4:
	print('Not enough arguments\n>>hostname,username,password required.')
else:
	address=sys.argv[1]
	username=sys.argv[2]
	password=sys.argv[3]
	param_ssh(address,username,password)	

