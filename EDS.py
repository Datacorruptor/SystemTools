import sys
import socket
from datetime import datetime

#define target
if len(sys.argv) ==2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print('Invalid syntax')
    sys.exit()

#banner
print('-'*50)
print("Target:"+target)
print('started:'+str(datetime.now()))
print('-'*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print('Checking port '+str(port))
        if result == 0:
            print("port "+str(port) +" is open")
        s.close()
except KeyboardInterrupt:
    print("Exiting programm")
    sys.exit()
except socket.gaierror:
    print("Hostname problem")
    sys.exit()
except socket.error:
    print("Coldnt connect to server")
    sys.exit()