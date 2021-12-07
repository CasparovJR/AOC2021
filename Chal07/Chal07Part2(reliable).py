import statistics as s
import math
def sumCalc(mean): return sum(abs(x-mean) * (abs(x-mean)+1)//2 for x in crabList)
crabList = [int(x) for x in open("Chal07.txt", 'r').read().strip().split(',')]
meanFloor, meanCeil = math.floor(s.mean(crabList)), math.ceil(s.mean(crabList))
print(min(sumCalc(meanFloor), sumCalc(meanCeil)))