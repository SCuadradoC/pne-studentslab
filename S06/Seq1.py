#from termcolor import colored
from termcolor import cprint

class dna():
    "A class for representing sequences"
    def __init__(self, seq:str, halt_on_error:bool = False):
        if type(seq) == str:
            for l in seq.upper():
                if not l in "ACTG \n":
                    if halt_on_error:
                        raise TypeError
                    else:
                        self.seq = "Invalid sequence"
                        break
            else:
                self.seq = seq.upper()
                print("New sequence created")
        elif halt_on_error:
            raise TypeError
        else:
            self.seq = "Invalid sequence"

    def __str__(self):
        return self.seq
    
    def len(self):
        return len(self.seq)

class Gene(dna):
    def __init__(self, name:str, seq:str):
        super().__init__(seq)
        self.name = name
        print("New gene created")
        
    def __str__(self):
        return self.name + " - " + self.seq


def print_seqs(sequences:list, color:str = "white"):
    out = ""
    n = 0
    for e in sequences:
        n += 1
        if type(e) != dna:
            out += f"Entry {n} - not a sequence"
        else:
            out += f"Sequence {n} : (Lenght: {e.len()}) {e}\n"
    cprint(out,color)

def generate_seqs(pat,rep):
    out = [dna(pat)]
    t = 0
    while rep > t:
        out.append(dna(str(out[t]) + pat))
        t += 1
    return out