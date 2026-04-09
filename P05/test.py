PATH = "./pages/"
page = open(PATH + "error.html")
contents = page.read()
page.close()
print(contents)