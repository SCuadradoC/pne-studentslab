seq = input("Enter the DNA sequence").lower()

bases_a = 0
bases_c = 0
bases_t = 0
bases_g = 0

for base in seq:
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

print("A: " + str(bases_a))
print("C: " + str(bases_c))
print("T: " + str(bases_t))
print("G: " + str(bases_g))