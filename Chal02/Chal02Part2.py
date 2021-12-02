with open("./Chal02.txt", "r") as f:
    h = 0
    d = 0
    a = 0

    for i in f.readlines():
        command, amount = i.split()[0], int(i.split()[1])
        if command == "down":
            a += amount
        elif command == "up":
            a -= amount
        else:
            h += amount
            d += a*amount
            
    print(h*d)