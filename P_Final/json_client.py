import http.client
import json
#import socket
import socketserver
from Seq1 import *
import os
#from config import *
import termcolor
from html_helper import *

IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
PORT = 8080
PATH = "./P_Final/html"
GENE_DIR = "./sequences/"
LNK = f"http://{IP}:{PORT}"
SERVER = "127.0.0.1:8080"

direction = input("Enter second part of the url here: ")

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", direction + "&json=1")
ens_data_raw = conn.getresponse().read().decode("utf-8")
ens_data = json.loads(ens_data_raw)

print(ens_data)
