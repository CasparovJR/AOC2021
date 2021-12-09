inp = [[int(x) for x in line] for line in open('Chal09.txt').read().strip().split()]
s = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        flag = False
        for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (0 <= i+k[0] < len(inp) and 0 <= j+k[1] < len(inp[0])):
                if inp[i][j] >= inp[i+k[0]][j+k[1]]:
                    flag = True
                    break

        if not flag:
            s += 1+int(inp[i][j])
print(s)