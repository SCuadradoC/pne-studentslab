import socket
from Seq2 import *
import os
#from config import *

IP = "212.128.255.85"
PORT = 8080
GENE_DIR = "./sequences/"

seqs = ["ATCGTACAGTCTGACTAGTCGGGGGTG",
        "TAGCGGGTCATGGGATCATATCGATGCTGCATTATT",
        "GCGAGCGATAGCAGTCTAGCTACGTA",
        "AGCGCGCGCCGTACGTGTCGTGCTATCGATCGTACGTCGATCGCGTAGTC",
        "TCTCGTAGCGAGAGCTAGCTAGTCCTTAGCTAGCGTGAGC"]

gene_files = os.listdir(GENE_DIR) #check after changing seq module
genes = {}
for e in gene_files:
    g = e.split(".")[0]
    genes.update({g:Seq(GENE_DIR + e)})
    


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
        print(f"Incoming message: {msg_in})")
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
                if cmd[1] in range(0,len(seqs)):
                    msg_out = seqs[cmd[1]]
                else:
                    msg_out = "Requested sequence outside database index"
                    
        elif com == "info":
            if len(cmd) != 2:
                msg_out = err
            else: #all this will change when i put my Seq1 in place of the borrowed one
                seq_in = Seq(cmd[1])
                if str(seq_in) == "Inv":
                    msg_out = "Invalid sequence"
                else:
                    msg_out = seq_in.count() #Rememeber to substitute function
                    
        elif com == "comp":
            if len(cmd) != 2:
                msg_out = err
            else:
                seq_in = Seq(cmd[1])
                msg_out = ""
        
        elif com == "rev":
            if len(cmd) != 2:
                msg_out = err
            else:
                seq_in = Seq(cmd[1])
                msg_out = ""
        
        elif com == "gene": #U5, ADA, FRAT1, FXN, RNU6_269P
            msg_out = "Revise"
        
        else:
            pass
        
        cs.send(msg_out)
        cs.close()

#if len(cmd) > 2:
#msg_out = "error: invalid command arguments"