import itertools
inp = []
folds = []

with open('Chal13.txt', 'r') as f:
    for i in f.readlines():
        if i != '\n':
            try:
                i = i.split(',')
                inp.append([int(i[0]), int(i[1])])
            except:
                i = i[0].split(' ')
                i = i[2]
                i = i.split('=')
                if i[0] == 'x':
                    for j in range(len(inp)):
                        if int(inp[j][0]) > int(i[1]):
                            dif = int(inp[j][0]) - int(i[1])
                            newCoord = int(i[1]) - dif
                            inp[j][0] = newCoord

                elif i[0] == 'y':
                    for j in range(len(inp)):
                        if int(inp[j][1]) > int(i[1]):
                            dif = int(inp[j][1]) - int(i[1])
                            newCoord = int(i[1]) - dif
                            inp[j][1] = newCoord

    inp.sort()
    inp = list(k for k,_ in itertools.groupby(inp))

paper = [['.' for _ in range(inp[-1][0]+1)] for _ in range(inp[-1][1]+1)]
for i in inp:
    paper[i[1]][i[0]] = '#'
for i in paper:
    print(*i)
