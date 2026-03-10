from pathlib import Path

def seq_ping():
    print("Module Seq0 working")

def seq_read_fasta(file:str):
    lines = Path(file).read_text().split("\n")
    l = len(lines)
    t = 1
    seq = ""
    while t < l:
        seq = seq + lines[t]
        t += 1
    return seq

def seq_len(sequence:str, isfile:bool = True):
    if isfile:
        seq = seq_read_fasta(sequence)
    else:
        seq = sequence
    return len(seq)
    
def seq_count_base(sequence:str, isfile:bool = True):
    if isfile:
        seq = seq_read_fasta(sequence)
    else:
        seq = sequence
    bases = {"A":0,"C":0,"T":0,"G":0}
    for l in seq:
        if l in bases:
            bases[l] += 1
    return bases

def seq_reverse(sequence:str):
    out = ""
    for e in sequence:
        out = e + out
    return out

def seq_complementary(sequence:str):
    out = ""
    comp = {"A":"T","C":"G","T":"A","G":"C"}
    for e in sequence:
        try:
            out += comp[e]
        except KeyError:
            out += "_"
    return out