with open('Chal08.txt','r') as f:
    sum = 0
    for i in f.readlines():
        i = i.strip().split(' | ')
        output = i[1].split()
        for i in output:
            if len(i) == 2 or len(i) == 4 or len(i) == 3 or len(i) == 7:
                sum += 1
    print(sum)
