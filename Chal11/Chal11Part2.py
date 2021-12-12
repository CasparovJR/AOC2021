inp = [[int(x) for x in line] for line in open('Chal11.txt').read().strip().split()]
step = 0

def dfs(i, j, inp, flashes, visited):
    for k in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        if (0 <= i+k[0] < len(inp) and 0 <= j+k[1] < len(inp[0])) and [i+k[0], j+k[1]] not in visited:
            inp[i+k[0]][j+k[1]] += 1

            if inp[i+k[0]][j+k[1]] > 9:
                visited.append([i+k[0], j+k[1]])
                inp, flashes, visited = dfs(i+k[0], j+k[1], inp, flashes, visited)
                inp[i+k[0]][j+k[1]] = 0
                flashes += 1

    return inp, flashes, visited

while True:
    visited = []
    flashes = 0
    #INITIAL
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            inp[i][j] += 1

    #DFS
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] > 9:
                visited.append([i, j])
                inp, flashes, visited = dfs(i, j, inp, flashes, visited)
                inp[i][j] = 0
                flashes += 1

    #CLEAN-UP
    for i in range(len(inp)):
        for j in range(len(inp[i])): 
            if inp[i][j] > 9:
                inp[i][j] = 0

    if flashes == len(inp)*len(inp[0]):
        print(step+1)
        break

    step += 1

