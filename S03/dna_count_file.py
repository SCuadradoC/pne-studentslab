def txt_read(path):
    file = open(path,"r")
    #out = file.read().split("\n")
    out = file.readlines()
    file.close()
    return out

line_n = 0
for seq in txt_read("dna_count_file.txt"):
    line_n += 1
    bases_a = 0
    bases_c = 0
    bases_t = 0
    bases_g = 0
    if len(seq) != 0:
        for base in seq:
            base = base.lower()
            if base == "a":
                bases_a += 1
            elif base == "c":
                bases_c += 1
            elif base == "t":
                bases_t += 1
            elif base == "g":
                bases_g += 1
            else:
                pass
        print("Line " + str(line_n) + " contains: A-" + str(bases_a) + ", C-" + str(bases_c) + ", T-" + str(bases_t) + ", G-" + str(bases_g))
