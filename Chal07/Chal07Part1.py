import statistics as s
crabList = [int(x) for x in open("Chal07.txt", 'r').read().strip().split(',')]
median = s.median(crabList)
fuel = sum(abs(median - pos) for pos in crabList)
print(fuel)