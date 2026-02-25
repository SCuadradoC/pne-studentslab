class matrix: #2d matrix
    def __init__(self, cont):
        if type(cont) == list:
            check = True
            size = []
            for row in cont:
                size.append(len(row))
                if check and type(row) != list:
                    check = False
                    break
                if check:
                    check = False
                    for e in row:
                        if type(e) not in [int,float]:
                            break
                    else:
                        check = True
        for e in size:
            if not e == size[0]:
                raise ValueError
        if check:
            self.cont = cont
            self.dim = (len(cont),len(cont[0]))
        else:
            raise TypeError
        
    def __str__(self):
        out = ""
        for row in self.cont:
            out += "|"
            for e in row:
                out += " "
                out += str(e)
                out += " "
            out += "|\n"
        return out
    
    def size(self):
        print(self.dim)
        
    #def matr_add(self,MatA,MatB):
    #    if 

#m1 = matrix([[1,3],[4,2]])
#print(m1)    
#m1.size()