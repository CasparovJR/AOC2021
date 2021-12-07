bingoNum = [int(x) for x in open('Chal04.txt').readline().strip().split(',')]
curBoard = []
earliestBingo = len(bingoNum)
earliestBingoBoard = []

def winCon(curBoard, earliestBingo, earliestBingoBoard):
    for i in curBoard:
        for j in i:
            if j not in bingoNum:
                break
                
        rightMost = -1
        for j in i:
            if rightMost < bingoNum.index(j):
                rightMost = bingoNum.index(j)

        if rightMost < earliestBingo:
            earliestBingo = rightMost
            earliestBingoBoard = curBoard

    return earliestBingo, earliestBingoBoard

with open('Chal04.txt', 'r') as f:
    for i, x in enumerate(f.readlines()[2:]):
        if (i+1)%6 > 0:
            l = x.strip().split(' ')
            l = [int(i) for i in l if i]
            curBoard.append(l)
        else:
            earliestBingo, earliestBingoBoard = winCon(curBoard, earliestBingo, earliestBingoBoard)
            earliestBingo, earliestBingoBoard = winCon(list(map(list, zip(*curBoard))), earliestBingo, earliestBingoBoard)

            curBoard = []

    s = 0
    for i in earliestBingoBoard:
        for j in i:
            if j not in bingoNum[:earliestBingo+1]:
                s+=j

    print(s*bingoNum[earliestBingo])