# ex13 reading
with open('pelican.txt', 'r') as inF:
    print(type(inF))
    #print(inF.read())
    #print(inF.readlines())
    for line in inF.readlines():
        if not line.isspace():
            print(line.rstrip())