#!/usr/bin/python3
import socket
import sys
import os

portnum=[21,22,23,25,80,8080]
exist=[]

def scan(portnum):
	
	try:	

		target=sys.argv[1]

		ip=socket.gethostbyname(target)
		print(portnum)
		for i in portnum:

			try:	
				print("[?]Working on port "+str(i)+"...")		
				sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				sock.settimeout(1)				
				r=sock.connect_ex((ip,i))			
				if(r == 0):
					exist.extend([i])
			except Exception as excp:
				print("")


			

	except Exception as e:
		print(e)
	finally:
		print("Open ports on "+target+" are: ")
		print(exist)
		
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("[-] Not Enough arguments.\n")
		usg()
	else:
		
		scan(portnum)



