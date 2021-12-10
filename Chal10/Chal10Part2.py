inp = [[x for x in line] for line in open('Chal10.txt').read().strip().split()]

scores = {')': 1, ']': 2, '}': 3, '>': 4}
dic2 = {'(': ')', '[': ']', '{': '}', '<': '>'}
dic = {')': '(', ']': '[', '}': '{', '>': '<'}
scoreList = []

for i in inp:
    lst = []
    flag = False
    s = ''
    score = 0
    for j in i:
        lst.append(j)
        if j in scores.keys() and dic[j] == lst[-2]:
            lst.pop()
            lst.pop()
        elif j in scores.keys() and dic[j] != lst[-2]:
            flag = True
            break # discard corrupted

    if not flag:
        for i in lst:
            s += dic2[i]

        for i in list(reversed(s)):
            score = (score * 5) + scores[i]

        scoreList.append(score)


print(sorted(scoreList)[int((len(scoreList)-1)/2)])