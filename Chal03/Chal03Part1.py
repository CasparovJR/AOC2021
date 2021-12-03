with open("Chal03.txt", 'r') as f:
    lZeroes = [0]*12
    lOnes = [0]*12
    for x in f.readlines():
        x = x.split()[0]
        for j, i in enumerate(x):
            if i == "1":
                lOnes[j] += 1
            if i == "0":
                lZeroes[j] += 1
    
    sCommon = ""
    sLeast = ""
    for k in range(len(lZeroes)):
        if lZeroes[k] > lOnes[k]:
            sCommon += "0"
            sLeast += "1"
        elif lOnes[k] > lZeroes[k]:
            sCommon += "1"
            sLeast += "0"

    print(int(sCommon, 2) * int(sLeast, 2))
            
