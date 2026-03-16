import socket
from Client0 import *

print("-----| Practice 3, Exercise 7 |------")

IP = "192.168.0.128"
PORT = 8080

c1 = Client(IP,PORT)

seq = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"

print(c1)

print("* Testing PING...")
print(c1.talk("ping"))

print("* Testing GET...")
for e in range(0,5):
    print(f"GET {e}:" + c1.talk(f"get {e}"))

print("* Testing INFO...")
print(f"Sequence: {seq}")
print(c1.talk(f"info {seq}"))

print("* Testing COMP...")
print(f"COMP {seq}")
print(c1.talk(f"comp {seq}"))

print("* Testing REV...")
print(f"REV {seq}")
print(c1.talk(f"rev {seq}"))

print("* Testing GENE...")
for e in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    pass