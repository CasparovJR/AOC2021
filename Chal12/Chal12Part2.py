from collections import Counter
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
        visited[index] += 1

    path.append(curPos)
    count = dict(Counter(path))

    if curPos == dest:
        allPaths.append(path)
    else:
        for i in dic[curPos]:

            index2, counter = list(dic.keys()).index(i), 0
            for k, v in count.items(): 
                counter += 1 if (k.islower() and v == 2) else 0

            if (visited[index2] < 2 and i != 'start' and counter <= 1):
                DFS(i, dest, visited, path, allPaths)

    path.pop()
    visited[index] -= 1

allPaths = []
DFS('start', 'end', [0]*len(dic.keys()), [], allPaths)
print(len(allPaths))
