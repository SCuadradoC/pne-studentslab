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

def listSpecies(params:dict):
    params.update({"name_selection":"common_name"}) #Until i add it as an input
    conn.request("GET", "/info/species?content-type=application/json")
    ens_data_raw = conn.getresponse().read().decode("utf-8")
    #print(ens_data_raw)
    ens_data = json.loads(ens_data_raw)["species"]
    if params["spec_lim"] != "":
        n = int(params["spec_lim"])
    else:
        n = -1 #starting at -1 n will never be 0
    
    names = ""
    for e in ens_data:
        names += f"<p>·{e[params["name_selection"]]}</p>"
        n += -1
        if n == 0:
            break
    
    contents = load_txt(PATH + "/page_template.html")
    contents = insert_content(contents,["title","content"],["List of species available in the database:",names])
    #print(contents)
    style = "text/html"
    return contents, style


def karyotype(params:dict):
    conn.request("GET", f"/info/assembly/{params["species"]}?content-type=application/json")
    ens_data_raw = conn.getresponse().read().decode("utf-8")
    #print(ens_data_raw)
    ens_data = json.loads(ens_data_raw)
    
    for e in ens_data:
        check = e
        break       #this gets the index of the first entry in the dictionary, to allow me to discard any invalid species
    
    contents = load_txt(PATH + "/page_template.html")
    if check != "error":
        names = ""
        for e in ens_data["karyotype"]:
            names += f"· {e}<br>"
        contents = insert_content(contents,["title","content"],[f"Chromosomes in the {params["species"]} karyotype:",names])
        #print(contents)
    else:
        contents = insert_content(contents,["title","content"],["Invalid species","The species you requested couldn't be found on the ensembl database "])
    style = "text/html"
    return contents, style

def chromosomeLenght(params:dict):
    conn.request("GET", f"/info/assembly/{params["species"]}?content-type=application/json")
    ens_data_raw = conn.getresponse().read().decode("utf-8")
    #print(ens_data_raw)
    ens_data = json.loads(ens_data_raw)
    
    for e in ens_data:
        check = e
        break       #this gets the index of the first entry in the dictionary, to allow me to discard any invalid species

    contents = load_txt(PATH + "/page_template.html")
    if check != "error":
        for e in ens_data["top_level_region"]:
            if e["name"] == params["chromosome"]:
                print(e)
                chrom_lenght = e["length"]
                contents = insert_content(contents,["title","content"],["Chromosome lenght info",f"Lenght of chromosome {params['chromosome']} of the {params["species"]} species is {str(chrom_lenght)} bases"])
                break
        else:
            contents = insert_content(contents,["title","content"],["Chromosome lenght info",f"The chromosome {params['chromosome']} doesn't exist in the {params["species"]} species"])
    else:
        contents = insert_content(contents,["title","content"],["Invalid species","The species you requested couldn't be found on the ensembl database "])
    style = "text/html"
    return contents, style


def geneLookup(params:dict):
    conn.request("GET", f"/xrefs/symbol/homo_sapiens/{params["gene"]}?content-type=application/json")
    ens_data_raw = conn.getresponse().read().decode("utf-8")
    #print(ens_data_raw)
    ens_data = json.loads(ens_data_raw)

    contents = load_txt(PATH + "/page_template.html")
    #if type(ens_data) == list:
    #    ens_data = ens_data[0]
    if len(ens_data) == 0:
        contents = insert_content(contents,["title","content"],["Search result",f"""The gene "{params["gene"]}" couldn't be found on the homo_sapiens genome """])
    #elif ens_data.get("error") != None:
    #    contents = insert_content(contents,["title","content"],["Search result",f"""The species {...} couldn't be found on the ensembl database """])
    else:
        ens_data = ens_data[0]
        #gene_id = ens_data["id"]
        contents = insert_content(contents,["title","content"],["Search result",f"The gene {params["gene"]} of homo_sapiens has the identifier {ens_data["id"]} "])
    style = "text/html"
    return contents, style