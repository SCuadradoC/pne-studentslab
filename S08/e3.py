import socket as sk

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.64"



while True:
    msg = input("Enter message: ")
    s = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    s.connect((IP,PORT))
    s.send(str.encode(msg))
    s.close()
    