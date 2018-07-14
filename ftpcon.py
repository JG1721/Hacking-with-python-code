
#!/usr/bin/python
import ftplib
import sys
def anoncheck(ip):
	try:
		ftp=ftplib.FTP(ip)
		ftp.login('anonymous',' ')
		print('\n[*]'+str(ip)+'Anonymous login successful')
		ftp.quit()
		return True
	except Exception as e:
		print("\n[-] Failed Login."+str(e))
		return False
if((len(sys.argv)) < 3):
	anoncheck(sys.argv[1])
else:
	print("Not enough arguments \n Usage: ftpcon.py hostname\n")
	exit()