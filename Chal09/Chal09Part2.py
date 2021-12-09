from functools import reduce
inp = [[int(x) for x in line] for line in open('Chal09.txt').read().strip().split()]
basins = []

def dfs(inp, i, j, s, visited):
    for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (0 <= i+k[0] < len(inp) and 0 <= j+k[1] < len(inp[0])):
            if int(inp[i+k[0]][j+k[1]]) != 9 and [i+k[0], j+k[1]] not in visited:
                visited.append([i+k[0], j+k[1]])
                s = dfs(inp, i+k[0], j+k[1], s+1, visited)
    return s


for i in range(len(inp)):
    for j in range(len(inp[i])):
        flag = False
        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (0 <= i+k[0] < len(inp) and 0 <= j+k[1] < len(inp[0])):
                if inp[i][j] >= inp[i+k[0]][j+k[1]]:
                    flag = True
                    break

        if not flag:
            basinSize = dfs(inp, i, j, 0, [])
            basins.append(basinSize)

basins.sort()
print(reduce(lambda x, y: x*y, basins[-3:]))