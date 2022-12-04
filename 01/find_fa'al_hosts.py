import nmap
import time

start = time.time()
network_add = input("Enter your Network Address : ").split('.')
start_range = input("Enter your Starting Number : ")
Last_num = input("Enter your Last Number : ")
nm = nmap.PortScanner()
f = open("Result_Fa'al_Hosts.txt", "a")
for i in range(int(start_range), int(Last_num) + 1) :
    ip = network_add[0] + '.' + network_add[1] + '.' + network_add[2] + '.' + str(i)
    scan_range = nm.scan(ip)
    scan = scan_range['scan']
    if scan != {} : 
        # print(f"IP {ip} is up")
        f.write(f"IP {ip} is up\n")

end = time.time()
estimation = end - start
f.write(estimation)
f.close()

