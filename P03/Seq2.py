from pathlib import Path
class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
        else:

            for ch in strbases:
                if ch != "A" and ch != "C" and ch != "T" and ch != "G":
                    self.strbases = "ERROR!"
                else:
                    self.strbases = strbases

        if self.strbases == "NULL":
            print("NULL sequence created")

        if self.strbases == "ERROR!":
            print("INVALID sequence!")

        if self.strbases == strbases:
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def length(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            return 0
        return self.strbases.count(base)

    def count(self):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for base in self.strbases:
            if base in bases:
                bases[base] = bases[base] + 1
        return bases

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            return self.strbases
        return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            complementary_sequence = self.strbases
        else:
            sequence2 = self.strbases
            complementary_sequence = ""

            for base in sequence2:
                if base == 'A':
                    complementary_sequence = complementary_sequence + "T"
                elif base == 'T':
                    complementary_sequence = complementary_sequence + "A"
                elif base == 'C':
                    complementary_sequence = complementary_sequence + "G"
                elif base == 'G':
                    complementary_sequence = complementary_sequence + "C"
                else:
                    complementary_sequence = complementary_sequence + base

        return complementary_sequence

    def seq_read_fasta(self, filepath):
        self.strbases = (Path(filepath).read_text())
        first_end = self.strbases.find("\n")
        seq1 = self.strbases[first_end:]
        seq1 = seq1.replace("\n", "")
        return seq1

    def frequency(self):
        if self.strbases == "NULL" or self.strbases == "ERROR!":
            return "Not valid sequence"


        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for base in self.strbases:
            if base in bases:
                bases[base] = bases[base] + 1

        valor_max = None
        freq_max = 0

        for base in bases:
            if bases[base] > freq_max:
                freq_max = bases[base]
                valor_max = base

        return valor_max