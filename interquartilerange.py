# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

req_arr = []

for a,b in zip(arr,freq):
    req_arr += [a]*b

req_arr = sorted(req_arr)

def median(arr, no):
    if (no % 2 == 0):
        x = no//2
        type(arr[x])
        return ((arr[x]+arr[x-1])/2)
    else:
        y = int((no+1)/2) 
        return arr[y-1]

def quartiles(arr, no):
    second_quartile = median(arr, no)

    first = [a for a in arr if a < second_quartile]

    third = [b for b in arr if b > second_quartile]

    first_quartile = median(first, len(first))

    third_quartile = median(third, len(third))

    return [first_quartile, third_quartile]

lst = quartiles(req_arr, len(req_arr))

print(lst[1] - lst[0])
