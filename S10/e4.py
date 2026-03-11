from Client0 import *
from config import *

IP = my_ip()
PORT = 8080

c1 = Client(IP,PORT)

for n in range(0,5):
    c1.talk(f"Message {n}")