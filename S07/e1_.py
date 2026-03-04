import socket as sk

PORT = 8081
IP = "212.128.255.94"

s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)

s.connect((IP,PORT))
msg = ""
while msg == "":
    msg = s.recv()
s.send(str.encode("Hello, server \n Checking from the client"))

s.close()