def fileread(path):
    file = open(path,"r").read()
    return file

print(fileread("test.txt"))