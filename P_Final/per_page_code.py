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
SERVER = "http://rest.ensembl.org"

conn = http.client.HTTPConnection(SERVER)

def listSpecies(params):
    conn.request("GET", "/info/species?content-type=application/json")
    ens_data_raw = conn.getresponse().read().decode("utf-8")
    #print(ens_data_raw)
    ens_data = json.loads(ens_data_raw)["species"]
    if params["spec_lim"] != "":
        n = params["spec_lim"]
    else:
        n = len(params)
    
    names = ""
    for e in ens_data:
        names += f"<p> {e} </p>"