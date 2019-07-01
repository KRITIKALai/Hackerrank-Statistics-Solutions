# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = sorted(list(map(int, input().split())))

def mean(arry, no):
    return sum(arr)/n

def median(arry, no):
    if (n % 2 == 0):
        x = int(n/2)
        return (arr[x]+arr[x-1])/2
    else:
        y = int((n+1)/2) 
        return arr[y]
def mode(arry, no):
    unique_elements = list(dict.fromkeys(arr))
    
    count_list = []

    for a in unique_elements:
        count = 0
        for b in arr:
            if (b == a):
                count += 1
        count_list.append(count)
    
    m = max(count_list) 
    req_indices = [i for i, j in enumerate(count_list) if j == m]

    lis = [arr[i] for i in req_indices]

    return (min(lis))

print(mean(arr,n))
print(median(arr,n))
print(mode(arr,n))