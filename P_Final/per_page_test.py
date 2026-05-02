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
SERVER = "rest.ensembl.org"


conn = http.client.HTTPConnection(SERVER)

params = {}
def listSpecies(params):
    contents = load_txt(PATH + "/page_template.html")
    return contents


def karyotype(params):
    contents = load_txt(PATH + "/page_template.html")
    return contents