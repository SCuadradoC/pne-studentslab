gene_files = os.listdir(GENE_DIR) #check after changing seq module
genes = {}
for e in gene_files:
    genes.update({e.split(".")[0] : GENE_DIR + e}) #this takes only the name of the gene from the list of gene files, and the directory where that file is
#print(genes)







for e in range(0,len(seqs)):
    options += f'<option value="{e}">{e}</option> '
    contents = contents.replace("[[options_seq]]",options)
    options = ""
    for e in genes:
        options += f'<option value="{e}">{e}</option> '
    contents = contents.replace("[[options_gene]]",options)









if "get_sequence" in self.path:
    req_val = int(self.path.split("=")[1])
    file = open(PATH + "/get.html")
    page_raw = file.read()
    file.close()
    contents = insert_content(page_raw,["n","seq_cont"],[str(req_val),seqs[req_val]])
    style = "text/html"
elif "get_gene" in self.path:
    req_val = self.path.split("=")[1]
    file = open(genes[req_val])
    gene_raw = file.read().split("\n")
    file.close()
    file = open(PATH + "/gene.html")
    page_raw = file.read()
    file.close()
    gene_proc = ""
    for e in gene_raw:
        gene_proc += f"{e}<br> "
    contents = insert_content(page_raw,["gene_name","gene_cont"],[req_val,gene_proc])
    file.close()
    style = "text/html"
    
    
    
    
    
    
    
    
    
            elif "/echo" in self.path:
                print(self.path)
                
                
            elif "operation" in self.path:
                req_val = self.path.split("?")[1].split("&")
                seq_in = Seq(req_val[0].split("=")[1],False)
                operation = req_val[1].split("=")[1]

                if operation == "Info":
                    bases = seq_in.count()
                    l = len(seq_in)
                    if l != 0:
                        result = f"""<p>Total length: {l}</p>
<p>A: {bases["A"]} ({bases["A"] / l * 100}%)</p>
<p>C: {bases["C"]} ({bases["C"] / l * 100}%)</p>
<p>T: {bases["T"]} ({bases["T"] / l * 100}%)</p>
<p>G: {bases["G"]} ({bases["G"] / l * 100}%)</p>"""
                    else:
                        seq_in = req_val[0].split("=")[1]
                        result = "Erroneous sequence"
                    
                elif operation == "Complement":
                    result = str(seq_in.complement())
                elif operation == "Reverse":
                    result = str(seq_in.reverse())
                file = open(PATH + "/operation.html")
                page_raw = file.read()
                file.close()