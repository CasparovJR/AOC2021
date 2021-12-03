with open("Chal03.txt", 'r') as f:
    bitCount = 0
    m = []
    l = []
    for x in f.readlines():
        x = x.split()[0]
        m.append(x)
        l.append(x)

    while bitCount < 12:
        zeroesCountj = 0
        onesCountj = 0

        zeroesCountk = 0
        onesCountk = 0

        for j in l:
            if j[bitCount] == "1":
                onesCountj += 1
            if j[bitCount] == "0":
                zeroesCountj += 1

        for k in m:
            if k[bitCount] == "1":
                onesCountk += 1
            if k[bitCount] == "0":
                zeroesCountk += 1

        if zeroesCountj > onesCountj:
            # zeroes more common, ones least common
            if len(l) > 1:
                l = list(filter(lambda a: a[bitCount] != '0', l))

        elif onesCountj >= zeroesCountj:
            if len(l) > 1:
                l = list(filter(lambda a: a[bitCount] != '1', l))

        if zeroesCountk > onesCountk:
            # Ones more common, ones least common
            if len(m) > 1:
                m = list(filter(lambda a: a[bitCount] != '1', m))

        elif onesCountk >= zeroesCountk:
            if len(m) > 1:
                m = list(filter(lambda a: a[bitCount] != '0', m))

        bitCount += 1

    print(int(l[0], 2) *  int(m[0], 2))