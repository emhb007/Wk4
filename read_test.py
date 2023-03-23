with open('test.txt','w') as myF:
    myF.write('Eoghan is class!\n')

# If you want to write to a different location -
#with open('D:\\test\\test.txt', 'r') as inF:

# Assuming test is in the same directory:
with open('test.txt', 'r') as inF:
    for line in inF.readlines():
        print(line)


