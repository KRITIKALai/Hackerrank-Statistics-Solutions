# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

l= list(input().split(" "))

a = int(l[0]) 
size = int(l[1]) 

pa = a/100

def ncr(n, r):
    return ((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))

required_probability1 = 0
for a in range(3):
    required_probability1 += ncr(10,a)*(pa ** a)*((1 - pa) ** (10-a))

required_probability2 = 0
for a in range(2, 11):
    required_probability2 += ncr(10,a)*(pa ** a)*((1 - pa) ** (10-a))

print("{:.3f}".format(required_probability1, 3))
print("{:.3f}".format(required_probability2, 3))