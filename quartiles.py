# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = sorted(list(map(int, input().split())))

def median(arr, n):
    if (n % 2 == 0):
        x = int(n/2)
        return (arr[x]+arr[x-1])/2
    else:
        y = int((n+1)/2) 
        return arr[y-1]

def quartiles(arr, n):
    second_quartile = int(median(arr, n))

    first = [a for a in arr if a < second_quartile]

    third = [b for b in arr if b > second_quartile]

    first_quartile = int(median(first, len(first)))

    third_quartile = int(median(third, len(third)))

    return [first_quartile, second_quartile, third_quartile]

lst = quartiles(arr, n)

print(*lst, sep = '\n')