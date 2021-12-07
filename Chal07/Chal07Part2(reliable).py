import statistics as s
import math
def sumCalc(mean): return sum(abs(x-mean) * (abs(x-mean)+1)//2 for x in crabList)
crabList = [int(x) for x in open("Chal07.txt", 'r').read().strip().split(',')]
print(min(sumCalc(math.floor(s.mean(crabList))), sumCalc(math.ceil(s.mean(crabList)))))