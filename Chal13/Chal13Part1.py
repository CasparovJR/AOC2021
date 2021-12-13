import itertools
inp = []
with open('Chal13.txt', 'r') as f:
    for i in f.readlines():
        if i != '\n':
            try:
                i = i.split(',')
                inp.append([int(i[0]), int(i[1])])
            except:
                i = i[0].split(' ')[2].split('=')
                if i[0] == 'x':
                    for j in range(len(inp)):
                        if int(inp[j][0]) > int(i[1]):
                            dif = int(inp[j][0]) - int(i[1])
                            newCoord = int(i[1]) - dif
                            inp[j][0] = newCoord

                    break # just the first fold, so break afterwards

    inp.sort()
    print(len(list(k for k,_ in itertools.groupby(inp))))