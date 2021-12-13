# Credit Leijurv and u/Waste_Willingness723 for the idea of a set
inp = set()
with open('Chal13.txt', 'r') as f:
    for i in f.readlines():
        if i != '\n':
            try:
                i = i.split(',')
                inp.add((int(i[0]), int(i[1])))
            except:
                i = i[0].split(' ')[2].split('=')
                if i[0] == 'x':
                    for j in list(inp):
                        if int(j[0]) > int(i[1]):
                            dif = int(j[0]) - int(i[1])
                            newCoord = int(i[1]) - dif
                            inp.remove(j)
                            inp.add((newCoord, j[1]))

                elif i[0] == 'y':
                    for j in list(inp):
                        if int(j[1]) > int(i[1]):
                            dif = int(j[1]) - int(i[1])
                            newCoord = int(i[1]) - dif
                            inp.remove(j)
                            inp.add((j[0], newCoord))

inp = list(inp)
inp.sort()

paper = [['.' for _ in range(inp[-1][0]+1)] for _ in range(inp[-1][1]+1)]
for i in inp:
    paper[i[1]][i[0]] = '#'
for i in paper:
    print(*i)
