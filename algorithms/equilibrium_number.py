t = int(input())

for _ in range(t):
    n = int(input())
    rsum =0
    a = list(map(int , input().split())) 
    
    rsum = sum(a)

    lsum = 0
    flag = -1
    for i in range(n):
        rsum -= a[i]
        if (rsum == lsum):
            flag = i
            break
        lsum += a[i]

    if (flag != -1):
        print(i+1)
    else:
        print('Not Found')

