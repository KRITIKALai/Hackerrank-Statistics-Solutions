# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
o1, o2 = list(map(float, input().split(" ")))

odds_ratio = o1/o2

pa = odds_ratio/(1 + odds_ratio)

required_probability = 0

def ncr(n, r):
    return ((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))

for a in range(3, 7):
    required_probability += ncr(6,a)*(pa ** a)*((1 - pa) ** (6-a))

print("{:.3f}".format(required_probability, 3))

