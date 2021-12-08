with open('Chal08.txt','r') as f:
    su = 0
    for i in f.readlines():
        segments = ['','','','','','','','','','']
        i = i.strip().split(' | ')
        input = i[0].split()
        output = i[1].split()
        # compare 1 with 4, get possible middle and top left segments -- known = [1, 4, 7, 8]
        middleBottomSeg = ''
        for i in input:
            if len(i) == 2:
                segments[1] = ''.join(sorted(i))
            if len(i) == 4:
                segments[4] = ''.join(sorted(i))
            if len(i) == 3:
                segments[7] = ''.join(sorted(i))
            if len(i) == 7:
                segments[8] = ''.join(sorted(i))
        for i in segments[4]:
            if i not in segments[1]:
                middleBottomSeg += i
        # compare this possible middle and top left segments with len(5) words, if both of those are in the word, then that word is 5 -- known = [1, 4, 5, 7, 8]
        for i in input:
            if len(i) == 5:
                if all(s in i for s in middleBottomSeg):
                    segments[5] = ''.join(sorted(i))
        # now compare 5 with 6, 0 and 9, find the differences, if there are 3 differences then the word is 0, otherwise if the word contains all of 1 then its 9
            #  otherwise its 6 -- known = [0, 1, 4, 5, 6, 7, 8, 9]
        for i in input:
            if len(i) == 6:
                count = 0
                for j in i:
                    if j not in segments[5]:
                        count+=1
                
                if count == 2:
                    segments[0] = ''.join(sorted(i))
                else:
                    count = 0
                    for j in segments[1]:
                        if j in i:
                            count += 1
                    if count == 2:
                        segments[9] = ''.join(sorted(i))
                    else:
                        segments[6] = ''.join(sorted(i))
        # now compare 4 with the other len(5) words, if theres 3 differences, then its 3, otherwise its 2 -- known = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in input:
            if len(i) == 5 and ''.join(sorted(i)) not in segments:
                count = 0
                for j in i:
                    if j not in segments[4]:
                        count+=1
                if count == 3:
                    segments[2] = ''.join(sorted(i))
                else:
                    segments[3] = ''.join(sorted(i))
        # now get the number
        s = ''
        for i in output:
            if ''.join(sorted(i)) in segments:
                s += str(segments.index(''.join(sorted(i))))
        su+=int(s)

    print(su)


