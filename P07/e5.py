import http.client
import json
import termcolor
from pathlib import Path
from Seq1 import *

PORT = 80
SERVER = 'rest.ensembl.org'

gene_lib = json.loads(Path("./P07/genes.json").read_text()) #I used a json file because it was easier than copying a dictionary in every program

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)
check = True

# gene_name = "FRAT1"
# gene_id = genes[gene_name]

for gene_name in gene_lib:
    gene_id = gene_lib[gene_name]
    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", f"/sequence/id/{gene_id}?content-type=application/json")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    #print(data1)

    # -- Create a variable with the data,
    # -- form the JSON received
    rj1 = json.loads(data1)
    gene = Seq(rj1["seq"])
    bases = gene.count()
    l = len(gene)

    mfb = ("",0)   #Most Frequent Base
    for e in bases:
        if bases[e] > mfb[1]:
            mfb = (e, bases[e])

    #print(f"Gene: {gene_name}\nDescription: {rj1["desc"]}\nBases: {rj1["seq"]}")

    print(f"""Total length: {l}
    A: {bases["A"]} ({round(bases["A"] / l * 100, 3)}%)
    C: {bases["C"]} ({round(bases["C"] / l * 100, 3)}%)
    T: {bases["T"]} ({round(bases["T"] / l * 100, 3)}%)
    G: {bases["G"]} ({round(bases["G"] / l * 100, 3)}%)
    Most frequent base: {mfb[0]}""")

