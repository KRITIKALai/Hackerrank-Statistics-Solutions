# Enter your code here. Read input from STDIN. Print output to STDOUT

frac_list = list(map(int,input().split(" ")))
defect = int(input())

num = frac_list[0]
den = frac_list[1]

p = num/den

probability = ((1-p) ** (defect-1)) * (p)

print("{:.3f}".format(probability))

