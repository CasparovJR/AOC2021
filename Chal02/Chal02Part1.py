with open("./Chal02.txt", "r") as f:
    h = 0
    d = 0

    for i in f.readlines():
        command, amount = i.split()[0], int(i.split()[1])
        if command == "forward":
            h += amount
        elif command == "down":
            d += amount
        else:
            d -= amount
            
    print(h*d)