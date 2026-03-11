class Seq():
    "A class for representing sequences"
    def __init__(self, seq:str, halt_on_error:bool = False):
        if type(seq) == str:
            for l in seq.upper():
                if not l in "ACTG \n":
                    if halt_on_error:
                        raise TypeError
                    else:
                        self.seq = "Inv"
                        break
            else:
                self.seq = seq.upper()
                print("New sequence created")
        elif halt_on_error:
            raise TypeError
        else:
            self.seq = "Inv"

    def __str__(self):
        return self.seq
    
    def len(self):
        return len(self.seq)

#class Gene(Seq):                               ### Not used
#    def __init__(self, name:str, seq:str):
#        super().__init__(seq)
#        self.name = name
#        print("New gene created")
#        
#    def __str__(self):
#        return self.name + " - " + self.seq


def print_seqs(sequences:list):
    out = ""
    n = 0
    for e in sequences:
        n += 1
        if type(e) != Seq:
            out += f"Entry {n} - not a sequence"
        else:
            out += f"Sequence {n} : (Lenght: {e.len()}) {e}\n"
    print(out)

def generate_seqs(pat,rep):
    out = [Seq(pat)]
    t = 0
    while rep > t:
        out.append(Seq(str(out[t]) + pat))
        t += 1
    return out