lant = []
with open('Chal06.txt','r') as f:
    for i in f.readlines():
        lant = i.strip().split(',')
    lant = list(map(int, lant))

sim = 0
while sim < 80:

    for i in range(len(lant)):
        if lant[i] >= 0:
            lant[i] -= 1

        if lant[i] == -1:
            lant[i] = 6
            lant.append(8)

    sim += 1
    print(sim)

print(len(lant))