import http.client
import json
#import socket
import socketserver
from Seq1 import *
import os
#from config import *
import termcolor
from html_helper import *

#IP = "127.0.0.1" #socket.gethostbyname(socket.gethostname())
#PORT = 8080
#PATH = "./P_Final/html"
#GENE_DIR = "./sequences/"
#LNK = f"http://{IP}:{PORT}"
#SERVER = "rest.ensembl.org"

###Note: I converted the code from functions to classes when starting with the advanced part. It took me about an hour (mostly copypaste and a few modifications
###like adding self. to all variables). This makes it very easy to add the json part but it can be done without it, it's just that I wanted to do it


class response:
    def __init__(self, params:dict, path:str, server:str = "rest.ensembl.org", IP = "127.0.0.1", PORT = 8080):
        self.params = params
        self.PATH = path
        self.LNK = f"http://{IP}:{PORT}"
        self.conn = http.client.HTTPConnection(server)
        self.source = ""
        self.contents = ""
        self.style = ""
    
    def __str__(self):  #These I used for debugging
        return f"Raw response, stored parameters:{str(self.params)}"
    
    def check_data(self):
        return [self.params, self.PATH, self.LNK, self.conn, self.source, self.contents]
    
    def load(self):     #Gets the info from the database
        self.conn.request("GET", self.source)
        ens_data_raw = self.conn.getresponse().read().decode("utf-8")
        try:
            ens_data = json.loads(ens_data_raw)
        except json.decoder.JSONDecodeError:
            ens_data = ens_data_raw
        
        if type(ens_data) == list:
            ens_data = ens_data[0]
        elif type(ens_data) == dict: #This allows me to detect when an attempt to access any info from the ensembl database returns an error or an empty json
            if len(ens_data) == 0:
                ens_data = ("error", "return_empty")
            elif len(ens_data) == 1:
                for e in ens_data: #this gets the index of the first entry in the dictionary
                    check = e
                    break
                if check == "error":
                    ens_data = (check, ens_data[check])
        
        self.ens_data = ens_data
    
    def is_id(self): #Checks if the gene entered is an ensembl stable identifier
        if len(self.params["gene"] ) != 15:
            return False
        else:
            check = True
        for n in range(0,4):
            if self.params["gene"][n] != "ENSG"[n]:
                check = False
                break
        if not check:
            try:
                int(self.params["gene"][4:15])
            except ValueError:
                check = False
        return check
    
    def get_id(self, return_id:bool = False):
        self.conn.request("GET", f"/xrefs/symbol/homo_sapiens/{self.params["gene"]}?content-type=application/json") #maybe add support for other species later (?)
        id_raw = self.conn.getresponse().read().decode("utf-8")
        id = json.loads(id_raw)
        if len(id) != 0:
            #print(id)
            self.id = id[0]["id"]
        else:
            self.id = ""

        if return_id:
            return self.id
    
    def html(self, template:str = "/page_template.html"):
        self.style = "text/html"
        file = open(self.PATH + template)
        self.contents = file.read()
        file.close()
        try:    #This tries to access the variable self.ens_data, and if it doesn't exist (.load() hasn't been used) it calls it itself (to avoid errors)
            self.ens_data
        except AttributeError:
            self.load()
        pass

    def json(self):
        self.style = "application/json"
        try:    #This tries to access the variable self.ens_data, and if it doesn't exist (.load() hasn't been used) it calls it itself (to avoid errors)
            self.ens_data
        except AttributeError:
            self.load()
    



class listSpecies(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.source = "/info/species?content-type=application/json"
    
    def __str__(self):
        return f"Response for listSpecies, stored parameters:{str(self.params)}"
    
    def html(self, template = "/page_template.html"):
        super().html(template)

        if self.params["spec_lim"] != "":
            n = int(self.params["spec_lim"])
        else:
            n = -1 #starting at -1 n will never be 0
        names = "        <div style='width: 1000px; height: 300px; overflow: auto; border: 1px solid #ccc; padding: 10px;'>\n"
        for e in self.ens_data["species"]:
            names += f"·{e[self.params["name_selection"]]}<br>\n"
            n += -1
            if n == 0:
                break
        names += "</div>"
        self.contents = insert_content(self.contents,["title","content"],["List of species available in the database:",names])
        return self.contents, self.style



class karyotype(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.source = f"/info/assembly/{params["species"]}?content-type=application/json"

    def __str__(self):
        return f"Response for karyotype, stored parameters:{str(self.params)}"
    
    def html(self, template = "/page_template.html"):
        super().html(template)
    
        if type(self.ens_data) != tuple:
            names = "        <div style='width: 1000px; height: 300px; overflow: auto; border: 1px solid #ccc; padding: 10px;'>\n"
            for e in self.ens_data["karyotype"]:
                names += f"· {e}<br>"
            names += "</div>"
            self.contents = insert_content(self.contents,["title","content"],[f"Chromosomes in the {self.params["species"]} karyotype:",names])
            #print(contents)
        else:
            self.contents = insert_content(self.contents,["title","content"],["Invalid species","The species you requested couldn't be found on the ensembl database "])
        return self.contents, self.style



class chromosomeLenght(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.source = f"/info/assembly/{params["species"]}?content-type=application/json"

    def __str__(self):
        return f"Response for chromosomeLenght, stored parameters:{str(self.params)}"
    
    def html(self, template = "/page_template.html"):
        super().html(template)
        
        if type(self.ens_data) != tuple:
            for e in self.ens_data["top_level_region"]:
                if e["name"] == self.params["chromosome"]:
                    #print(e)
                    chrom_lenght = e["length"]
                    self.contents = insert_content(self.contents,["title","content"],["Chromosome lenght info",f"Lenght of chromosome {self.params['chromosome']} of the {self.params["species"]} species is {str(chrom_lenght)} bases"])
                    break
            else:
                self.contents = insert_content(self.contents,["title","content"],["Chromosome lenght info",f"The chromosome {self.params['chromosome']} doesn't exist in the {self.params["species"]} species"])
        else:
            self.contents = insert_content(self.contents,["title","content"],["Invalid species","The species you requested couldn't be found on the ensembl database "])
        return self.contents, self.style



class geneLookup(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        self.source = f"/xrefs/symbol/homo_sapiens/{params["gene"]}?content-type=application/json" #maybe add support for other species later (?)

    def __str__(self):
        return f"Response for geneLookup, stored parameters:{str(self.params)}"
    
    def html(self, template = "/page_template.html"):
        #super().html(template)   #I won't use super because geneLookup in particular only requests the id of the gene, which I implement with the get_id() function
        file = open(self.PATH + template)
        self.contents = file.read()
        file.close()

        try:
            self.id
        except:
            self.get_id()
            
        if self.id == "":
            self.contents = insert_content(self.contents,["title","content"],["Search result",f"""The gene "{self.params["gene"]}" couldn't be found on the homo_sapiens genome """])
        #elif ens_data.get("error") != None:
        #    contents = insert_content(contents,["title","content"],["Search result",f"""The species {...} couldn't be found on the ensembl database """])
        else:
            #gene_id = ens_data["id"]
            self.contents = insert_content(self.contents,["title","content"],["Search result",f"The gene {self.params["gene"]} of homo_sapiens has the identifier {self.id} "])
        
        return self.contents, self.style


class geneSeq(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        
        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id(params["gene"])
        self.source = f"/sequence/id/{self.id}?content-type=application/json"

    def __str__(self):
        return f"Response for geneSeq, stored parameters:{str(self.params)}"
    
    def html(self, template = "/page_template.html"):
        super().html(template)
        body_text = f"""{self.id}<br>
        <div style='width: 1000px; height: 300px; overflow: auto; border: 1px solid #ccc; padding: 10px;'>
        """
        for e in self.ens_data["seq"]:
            body_text += e + "<wbr>"
        body_text += "</div>"
        self.contents = insert_content(self.contents,["title","content"],["Gene requested:",body_text])
        
        return self.contents, self.style    


class geneInfo(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)

        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id(params["gene"])
        self.source = f"/sequence/id/{self.id}?content-type=application/json"
    
    def __str__(self):
        return f"Response for geneInfo, stored parameters:{str(self.params)}"
    
    def create_info_table(self):
        coordinates = self.ens_data["desc"].split(":")
        print(self.ens_data)
        self.table = {
            "molecule":self.ens_data["molecule"],
            "location":f"{coordinates[0]} {coordinates[2]}",
            "reference_version":coordinates[1],
            "start_base":coordinates[3],
            "end_base":coordinates[4],
            "len":int(coordinates[4]) - int(coordinates[3]),
            "strand_orientation":{"1":"forward","-1":"reverse"}[coordinates[5]]
        }
    
    def html(self, template = "/page_template.html"):
        super().html(template)
        try:
            self.table
        except AttributeError:
            self.create_info_table()
        
        body_text = f"""<p>Molecule type: {self.table["molecule"]}</p>
<p>Located in {self.table["location"]}</p>
<p>From base {self.table["start_base"]} to {self.table["end_base"]}</p>
<p>Total length: {self.table["len"]}</p>
<p>Strand orientation: {self.table["strand_orientation"]}</p>
<p>Genome reference version: {self.table["reference_version"]}</p>
"""
        self.contents = insert_content(self.contents,["title","content"],["Info from the gene requested",body_text])
        
        return self.contents, self.style


class geneCalc(response):
    def __init__(self, params, path, server = "rest.ensembl.org", IP="127.0.0.1", PORT=8080):
        super().__init__(params, path, server, IP, PORT)
        
        if self.is_id():
            self.id = params["gene"]
        else:
            self.get_id(params["gene"])
        self.source = f"/sequence/id/{self.id}?content-type=application/json"
    
    def __str__(self):
        return f"Response for geneCalc, stored parameters:{str(self.params)}"
    
    def count(self):
        bases = {"A":0,"C":0,"T":0,"G":0}
        seq = self.ens_data["seq"]
        try:
            for l in seq:
                bases[l] += 1
        except KeyError:
            bases = {"A":0,"C":0,"T":0,"G":0}
        return bases
    
    def html(self, template = "/page_template.html"):
        super().html(template)
        n = self.count()
        body_text = f"""·Lenght: {len(self.ens_data["seq"])}
·A: {n["A"]}
·C: {n["C"]}
·T: {n["T"]}
·G: {n["G"]}"""
        self.contents = insert_content(self.contents,["title","content"],["Calculation result:",body_text])
        
        return self.contents, self.style