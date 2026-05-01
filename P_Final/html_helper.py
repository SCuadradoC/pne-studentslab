def insert_content(content:str, template:list, data:list):
    if type(template) != list:
        template = [template]
    if type(data) != list:
        data = [data]
    if len(template) != len(data):
        return
    #print(template)
    #print(data)
    for n in range(0,len(template)):
        content = content.replace(f"[[{template[n]}]]",data[n])
    return content

def parse_req(path:str):
    n = 1
    page = ""
    param = {}
    while path[0] != "?":
        page += path[0]
        path = path[1:]
        if len(path) == 0:
            break
    else:
        path = path[1:]
        for e in path.split("&"):
            i = e.split("=")
            param.update({i[0]:i[1]})
    return page,param