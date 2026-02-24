class dna_seq():
    "A class for representing sequences"
    def __init__(self, seq:str):
        if type(seq) == str:
            for l in seq.upper():
                if not l in "ACTG":
                    raise TypeError
            else:
                self.seq = seq.upper()
                print("New sequence created")
        else:
            raise TypeError

    def __str__(self):
        return self.seq
    
    def len(self):
        return len(self.seq)

class Gene(dna_seq):
    def __init__(self, name:str, seq:str):
        super().__init__(seq)
        self.name = name
        print("New gene created")
        
    def __str__(self):
        return self.name + " - " + self.seq
        