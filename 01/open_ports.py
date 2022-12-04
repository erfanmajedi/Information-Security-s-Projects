import socket
from datetime import datetime

target = input('Enter the remote host IP to scan : ')
start_port_number = int(input('Enter The Start Port Number :'))
last_port_number = int(input('Enter The last Port Number :')) 

 
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))

f = open('Result_open_ports.txt', 'a')
try:
    
    for port in range(start_port_number,last_port_number + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0 :
            f.write(f"Port {port} is open")
        else : 
            print(f'Port {port} shoma yaft nashod :)')
        
        s.close()
    f.close()
except :
    pass
         