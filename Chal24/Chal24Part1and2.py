from z3 import *
def gen():
    inp = [x.strip().split() for x in open('Chal24.txt').readlines()]
    counter = 1
    majorCounter = 0
    l = []
    stack = []

    for i, x in enumerate(inp):
        if i % 18 == 0:
            if len(l) == 2:
                stack.append(l)
            majorCounter += 1
            l = []
            counter = 1

        if (counter == 6):
            l.append(x[2])

        if (counter == 16) and len(l) == 1:
            l.append(x[2])

        counter+=1

    counter = 0
    stack2 = []
    finalInputs = []
    while counter < 14:
        if int(stack[counter][0]) > 0:
            stack2.append([counter, stack[counter][1]])
        elif int(stack[counter][0]) < 0:
            popped_value = stack2.pop()
            finalInputs.append(f"in{popped_value[0]} + {int(stack[counter][0])+int(popped_value[1])} == in{counter}")

        counter+=1

    return finalInputs


maxSol = [0 for _ in range(14)]
minSol = [0 for _ in range(14)]
def opti(s, ss, x, y):
    mmx = s.maximize(globals()[x])
    mmy = s.maximize(globals()[y])
    minx = ss.minimize(globals()[x])
    miny = ss.minimize(globals()[y])

    while s.check() == sat:
        maxSol[int(x.split('in')[1])] = str(mmx.value())
        maxSol[int(y.split('in')[1])] = str(mmy.value())

    while ss.check() == sat:
        minSol[int(x.split('in')[1])] = str(minx.value())
        minSol[int(y.split('in')[1])] = str(miny.value())

def main():
    finalInputs = gen()
    for z in finalInputs:
        s = Optimize()
        ss = Optimize()
        x = z.split(' + ')[0]
        y = z.split(' == ')[1]
        globals()[x], globals()[y] = Ints(f'{x}, {y}')
        s.set(priority='pareto')
        s.add(eval(z), globals()[x] <= 9, globals()[y] <= 9, globals()[x] >= 1, globals()[y] >= 1)
        ss.set(priority='pareto')
        ss.add(eval(z), globals()[x] <= 9, globals()[y] <= 9, globals()[x] >= 1, globals()[y] >= 1)

        opti(s, ss, x, y)
    
    print(''.join(maxSol), ''.join(minSol))

main()