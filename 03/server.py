import socket
import sys

host = '127.0.0.1'
port = 8080

command_line = ''
send_command = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn : 
        print(f'connceted by {addr}')
        while True : 
            data = conn.recv(4096)
            if not data : 
                break
            print(data.decode('utf-8'))
            command_line = input("Command ( Enter E for exit) : ")
            if command_line == 'sysimfo' : 
                send_command = 'You are Hacked !!'
            else : 
                if command_line == 'e' : 
                    sys.exit()
            if send_command != '' : 
                conn.send(send_command)
            data = conn.recv(4096)
            print(data.decode('utf-8'))