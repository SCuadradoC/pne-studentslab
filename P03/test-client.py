import socket
from Client0 import *

print("-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
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

print("\n* Testing GENE...\n")
for e in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    print(f"Gene {e}:")
    print(c1.talk(f"gene {e}")[0:100]) #added the range to avoid filling the command line and covering the other results
    print()