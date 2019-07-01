# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = sorted(list(map(int, input().split())))

def mean(arr, n):
    return (sum(arr)/n)

def standard_deviation(arr, n):
    m = mean(arr,n)
    num = 0
    den = n

    for a in arr:
        num += (m - a)**2
    
    val = (num/den) ** 0.5

    return val

print("{:.1f}".format(standard_deviation(arr, n)))