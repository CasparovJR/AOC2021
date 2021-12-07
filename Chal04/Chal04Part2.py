bingoNum = [int(x) for x in open('Chal04.txt').readline().strip().split(',')]
curBoard = []
earliestBingos = []

def winCon(curBoard, curEarliestBingo, curEarliestBingoBoard):
    curEarliestBingo = len(bingoNum)
    curEarliestBingoBoard = []

    for i in curBoard:
        for j in i:
            if j not in bingoNum:
                break
                
        rightMost = -1
        for j in i:
            if rightMost < bingoNum.index(j):
                rightMost = bingoNum.index(j)

        if rightMost < curEarliestBingo:
            curEarliestBingo = rightMost
            curEarliestBingoBoard = curBoard

    return curEarliestBingo, curEarliestBingoBoard

with open('Chal04.txt', 'r') as f:
    for i, x in enumerate(f.readlines()[2:]):
        if (i+1)%6 > 0:
            l = x.strip().split(' ')
            l = [int(i) for i in l if i]
            curBoard.append(l)
        else:
            curEarliestBingo, curEarliestBingoBoard = winCon(curBoard, 0, [])
            curEarliestBingo, curEarliestBingoBoard = winCon(list(map(list, zip(*curBoard))), curEarliestBingo, curEarliestBingoBoard)
            earliestBingos.append([curEarliestBingo, curEarliestBingoBoard])
            curBoard = []

    latestBingo = -1
    latestBingoBoard = []
    for x in earliestBingos:
        if x[0] > latestBingo:
            latestBingo = x[0]
            latestBingoBoard = x[1]

    s = 0
    for i in latestBingoBoard:
        for j in i:
            if j not in bingoNum[:latestBingo+1]:
                s+=j

    print(s*bingoNum[latestBingo])