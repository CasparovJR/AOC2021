from collections import Counter
dic = Counter({-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0})
dic.update(int(x) for x in open('Chal06.txt').read().strip().split(','))

sim = 0
while sim < 256:
    for i in dic:
        if i < 8:
            dic[i] = dic[i+1]
        if i == 7:
            dic[i+1] = dic[-1]

    dic[6] += dic[-1]
    dic[-1] = 0
    sim+=1

print(sum(dic.values()))