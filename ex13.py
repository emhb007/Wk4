# write_file

with open('pelican.txt','a') as myF:
    myF.write('A wonderful bird is the pelican,\n')
    myF.write('His bill holds more than his belican.')
    lines = ['He can take in his beak, \n','Enough food for a week\n',
             'but I\'m damned if I see how the helican. \n']
    myF.writelines(lines)