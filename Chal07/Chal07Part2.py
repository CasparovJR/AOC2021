import statistics as s
crabList = [int(x) for x in open("Chal07.txt", 'r').read().strip().split(',')]
mean = int(s.mean(crabList))
print(mean, s.mean(crabList))
fuel = sum(abs(x-mean) * (abs(x-mean)+1)//2 for x in crabList)
print(fuel)