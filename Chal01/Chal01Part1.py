with open("./Chal01.txt", "r") as f:
    before = 0
    after = 0
    increased = 0
    
    for i in f.readlines():
        after = int(i.split()[0])
        if after > before and before != 0:
            increased += 1
        before = after

    print(increased)