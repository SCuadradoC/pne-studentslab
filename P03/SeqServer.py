import socket
from Seq1 import *
import os
#from config import *

IP = "127.0.0.1"
PORT = 8080
GENE_DIR = "../sequences/"

seqs = ["ATCGTACAGTCTGACTAGTCGGGGGTG",
        "TAGCGGGTCATGGGATCATATCGATGCTGCATTATT",
        "GCGAGCGATAGCAGTCTAGCTACGTA",
        "AGCGCGCGCCGTACGTGTCGTGCTATCGATCGTACGTCGATCGCGTAGTC",
        "TCTCGTAGCGAGAGCTAGCTAGTCCTTAGCTAGCGTGAGC"]

gene_files = os.listdir(GENE_DIR) #check after changing seq module
genes = {}
for e in gene_files:
    genes.update({e.split(".")[0] : GENE_DIR + e}) #this takes only the name of the gene from the list of gene files, and the directory where that file is
#print(genes)


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to avoid problem if the socket takes a while to clear

ls.bind((IP, PORT))
ls.listen()
print("Server configured and running")


#logs = []
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print(f"Client connecnted. IP and Port: {client_ip_port}")
        #logs.append(f"Client {conn}: {client_ip_port}")
        
        msg_in = cs.recv(2048).decode()
        print(f"Incoming message: '{msg_in}'")
        cmd = msg_in.strip().split(" ")
        com = cmd[0].lower()
        err = "Invalid command arguments"
        
        if com == "ping":         # PING GET INFO COMP REV GENE
            if len(cmd) == 1:
                msg_out = "OK"
            else:
                msg_out = err
                
        elif com == "get" :
            if len(cmd) != 2:
                msg_out = err
            else:
                try:
                    msg_out = seqs[int(cmd[1])]
                except ValueError:
                    msg_out = err
                except IndexError:
                    msg_out = "Requested sequence outside database index"
                    
        elif com == "info":
            if len(cmd) != 2:
                msg_out = err
            else: 
                seq_in = Seq(cmd[1])
                if not seq_in.is_valid():
                    msg_out = "Invalid sequence"
                else:
                    bases = seq_in.count()
                    l = len(seq_in)
                    msg_out = f"""Sequence: {str(seq_in)}
Total length: {l}
A: {bases["A"]} ({bases["A"] / l * 100}%)
C: {bases["C"]} ({bases["C"] / l * 100}%)
T: {bases["T"]} ({bases["T"] / l * 100}%)
G: {bases["G"]} ({bases["G"] / l * 100}%)"""
                    
        elif com == "comp":
            if len(cmd) != 2:
                msg_out = err
            else:
                seq_in = Seq(cmd[1])
                msg_out = str(seq_in.complement())
        
        elif com == "rev":
            if len(cmd) != 2:
                msg_out = err
            else:
                seq_in = Seq(cmd[1])
                msg_out = str(seq_in.reverse())
        
        elif com == "gene": #U5, ADA, FRAT1, FXN, RNU6_269P
            if len(cmd) != 2:
                msg_out = err
            else:
                try:
                    s = Seq()
                    s.read_fasta(genes[cmd[1]])

                    msg_out = str(s)
                except KeyError:
                    msg_out = "Gene not available"
        
        else:
            pass
        
        cs.send(str.encode(msg_out + "\n"))
        cs.close()

#if len(cmd) > 2:
#msg_out = "error: invalid command arguments"