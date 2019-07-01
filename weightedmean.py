# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

arr = list(map(int, input().split()))
wt = list(map(int, input().split()))
num = 0
den = 0

for a, b in zip(arr, wt):
    num += (a*b)
    den += b

print("{:.1f}".format(num/den))
