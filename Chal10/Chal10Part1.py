inp = [[x for x in line] for line in open('Chal10.txt').read().strip().split()]

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
dic = {')': '(', ']': '[', '}': '{', '>': '<'}
lst = []
s = 0
for i in inp:
    for j in i:
        lst.append(j)
        if j in scores.keys() and dic[j] == lst[-2]:
            lst.pop()
            lst.pop()
        elif j in scores.keys() and dic[j] != lst[-2]:
            s += scores[j]
            break # find first one
print(s)