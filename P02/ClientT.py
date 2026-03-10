import socket
from time import sleep

class Client:
    def __init__(self, ip:str, port:int, brk:bool = False):
        self.valid = True
        if type(ip) == str:
            ip_list = ip.split(".")
        else:
            print("Invalid ip")
            self.valid = False
            if brk:
                raise TypeError
        
        if len(ip_list) == 4:
            for e in ip_list:
                if int(e) not in range(0,256):
                    print("Invalid ip")
                    self.valid = False
                    if brk:
                        raise ValueError
                    break
            else:
                self.ip = ip
        
        try:
            self.port = int(port)
        except ValueError:
            if brk:
                raise
            else:
                print("Invalid port")
                self.valid = False
                if brk:
                    raise ValueError
        
        if self.valid:
            self.sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #print("Client created")
            
        
    
    def __str__(self):
        return f"Connection to SERVER at {str(self.ip)}, PORT: {str(self.port)}"
    
    def ping(self):
        print("OK")
    
    def talk(self, msg):
        print(msg[0:10])