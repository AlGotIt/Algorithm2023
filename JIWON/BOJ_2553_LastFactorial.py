import math
n = int(input())

a = math.factorial(n)

s = str(a).replace("0","")

print(s[-1])