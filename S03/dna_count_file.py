def txt_read(path):
    file = open("S03/" + path,"r")
    #out = file.read().split("\n")
    out = file.readlines()
    file.close()
    return out

line_n = 0
for seq in txt_read("dna_count_file.txt"):
    line_n += 1
    bases = {"A":0,"C":0,"T":0,"G":0}
    if seq[0] != "\n":
        for e in seq:
            if e in bases:
                bases[e] += 1
        mesg = "Line " + str(line_n) + " contains: "
        for e in bases:
            mesg = mesg + " " + e + "-" + str(bases[e]) 
        print(mesg)
