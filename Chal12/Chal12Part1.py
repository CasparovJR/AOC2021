inp = [x.split('-') for x in open('Chal12.txt').read().strip().split()]
dic = {}
for i in [x.split('-') for x in open('Chal12.txt').read().strip().split()]:
    dic[i[0]] = [] if i[0] not in dic.keys() else dic[i[0]]
    dic[i[1]] = [] if i[1] not in dic.keys() else dic[i[1]]
    dic[i[0]].append(i[1])
    dic[i[1]].append(i[0])

def DFS(curPos, dest, visited, path, allPaths):
    path = list(path)
    index = list(dic.keys()).index(curPos)

    if curPos.islower():
        visited[index] = True

    path.append(curPos)

    if curPos == dest:
        allPaths.append(path)
    else:
        for i in dic[curPos]:
            index2 = list(dic.keys()).index(i)
            if visited[index2] == False:
                DFS(i, dest, visited, path, allPaths)

    path.pop()
    visited[index] = False

allPaths = []
DFS('start', 'end', [False]*len(dic.keys()), [], allPaths)
print(len(allPaths))
