import os

# ping of specific ip 
with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park}  \n")
    # ping for each ip in the file

f = open("result_ping.txt","a")
for ip in park:
    response = os.popen(f"ping {ip} ").read()
    
    #saving some ping output details to output file
    
    if("Request timed out." or "unreachable") in response:
        print(response)
        f.write(response)
        f.write(str(ip) + ' link is down'+'\n')
    else:
        print(response) 
        f.write(response)
        f.write(str(ip) + ' is up '+'\n')
f.close() 



