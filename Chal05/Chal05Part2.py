ventDiagram = []
largestX = 0
largestY = 0

with open("Chal05.txt", 'r') as f:
    for i in f.readlines():
        coords = i.strip().split(' -> ')
        coords = [coords[0].split(','), coords[1].split(',')]
        #coords = [j for i in coords for j in i]
        maximumX = max(list(map(lambda x: int(x[0]), coords)))
        maximumY = max(list(map(lambda x: int(x[1]), coords)))

        if maximumX >= largestX:
            largestX = maximumX
        if maximumY >= largestY:
            largestY = maximumY

    ventDiagram = [[0 for _ in range(largestX+1)] for _ in range(largestY+1)]

with open("Chal05.txt", 'r') as f:
    overlap = 0
    for i in f.readlines():
        coords = i.strip().split(' -> ')
        coords = [coords[0].split(','), coords[1].split(',')]
        x = list(map(lambda k: int(k[0]), coords))
        y = list(map(lambda k: int(k[1]), coords))
        minX, maxX = min(x[0],x[1]), max(x[0],x[1])
        minY, maxY = min(y[0],y[1]), max(y[0],y[1])
        
        dx = 1 if x[0]-x[1] < 0 else -1 if x[0]-x[1] > 0 else 0
        dy = 1 if y[0]-y[1] < 0 else -1 if y[0]-y[1] > 0 else 0

        # generate points in the line
        while x[0] != x[1] or y[0] != y[1]:
            ventDiagram[y[0]][x[0]] += 1

            if ventDiagram[y[0]][x[0]] == 2:
                overlap += 1

            x[0] += dx
            y[0] += dy

            if x[0] == x[1] and y[0] == y[1]:
                ventDiagram[y[0]][x[0]] += 1
                if ventDiagram[y[0]][x[0]] == 2:
                    overlap += 1
    
    print(overlap)


