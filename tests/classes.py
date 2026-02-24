class matrix: #2d matrix
    def __init__(self, dim:tuple, cont):
        if type(dim) == tuple:
            self.dim = dim
        else:
            raise TypeError("Dim must be a tuple")
        if type(cont) == list:
            if len(cont) != dim[0]:
                check = False
                mesg = "dim incorrectly defined"
            
            for row in cont:
                check = not len(row) == cont
                if not check and type(row) != list:
                    break
                if not check:
                    for e in row:
                        check = True
                        if type(e) not in [int,float]:
                            break
                    else:
                        check = False
            else:
                check = True
        
            

    def __str__(self):
        out = ""
        for row in self.cont:
            out += "|  "
            for e in row:
                out += str(e)
                out += "  "
            out += "|\n"
        return out
    
    #def matr_add(self,MatA,MatB):
    #    if 


            
