with open("./Chal01.txt", "r") as f:
    l = []
    s = 0

    before = 0
    after = 0
    increased = 0

    for i in f.readlines():
        s = int(i.split()[0])
        l.append(s)

        if len(l) == 3:
            after = sum(l)
            l.pop(0)

            if after > before and before != 0:
                increased += 1

            before = after
            
    print(increased)