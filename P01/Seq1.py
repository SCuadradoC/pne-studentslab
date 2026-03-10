from pathlib import Path

class Seq:
    def __init__(self, cont:str = ""):
        self.valid = False
        if type(cont) != str:
            raise ValueError
        if len(cont) == 0:
            print("Null sequence created")
            self.cont = "NULL"
        else:
            for e in cont:
                if e.upper() not in "ACTG \n":
                    print("Invalid sequence")
                    self.cont = "ERROR"
                    break
            else:
                self.cont = cont.upper()
                self.valid = True
                print("New sequence created")
    
    def __str__(self):
        return self.cont
    
    def read_fasta(self, file:str):
        lines = Path(file).read_text().split("\n")
        l = len(lines)
        t = 1
        seq = ""
        while t < l:
            seq = seq + lines[t]
            t += 1
        self.cont = seq
        self.valid = True

    def len(self):
        if self.valid:
            return len(self.cont)
        else:
            return 0
    
    def count(self):
        bases = {"A":0,"C":0,"T":0,"G":0}
        if self.valid:
            for l in self.cont:
                if l in bases:
                    bases[l] += 1
        return bases

    def count_base(self):
        bases = self.count()
        print(f"A:{bases["A"]}    C:{bases["C"]}    T:{bases["T"]}    G:{bases["G"]}")

    def reverse(self):
        if self.valid:
            out = ""
            for e in self.cont:
                out = e + out
        else:
            out = self.cont
        return out

    def complement(self):
        table = {"A":"T","T":"A","C":"G","G":"C"}
        if self.valid:
            out = ""
            for e in self.cont:
                out += table[e]
        else:
            out = self.cont
        return out